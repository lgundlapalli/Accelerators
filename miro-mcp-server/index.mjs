#!/usr/bin/env node

import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';
import { MiroClient } from './miro-client.mjs';

const token = process.env.MIRO_API_TOKEN;
if (!token) {
  console.error('Error: MIRO_API_TOKEN environment variable is required');
  process.exit(1);
}

const miro = new MiroClient(token);

const server = new McpServer({
  name: 'miro',
  version: '1.0.0',
});

// === Board Tools ===

server.tool(
  'miro_list_boards',
  'List all Miro boards accessible to the authenticated user',
  {},
  async () => {
    const result = await miro.listBoards();
    const boards = result.data.map((b) => `- ${b.name} (id: ${b.id})`).join('\n');
    return { content: [{ type: 'text', text: boards || 'No boards found' }] };
  },
);

server.tool(
  'miro_get_board',
  'Get details of a specific Miro board',
  { board_id: z.string().describe('The Miro board ID') },
  async ({ board_id }) => {
    const board = await miro.getBoard(board_id);
    return { content: [{ type: 'text', text: JSON.stringify(board, null, 2) }] };
  },
);

server.tool(
  'miro_create_board',
  'Create a new Miro board',
  {
    name: z.string().describe('Board name'),
    description: z.string().optional().describe('Board description'),
  },
  async ({ name, description }) => {
    const board = await miro.createBoard(name, description || '');
    return {
      content: [
        {
          type: 'text',
          text: `Board created: "${board.name}" (id: ${board.id})\nURL: ${board.viewLink}`,
        },
      ],
    };
  },
);

// === Item Reading ===

server.tool(
  'miro_get_board_items',
  'Get all items on a Miro board',
  {
    board_id: z.string().describe('The Miro board ID'),
    limit: z.number().optional().describe('Max items to return (default 50)'),
  },
  async ({ board_id, limit }) => {
    const result = await miro.getBoardItems(board_id, limit || 50);
    return { content: [{ type: 'text', text: JSON.stringify(result.data, null, 2) }] };
  },
);

// === Sticky Notes ===

server.tool(
  'miro_create_sticky_note',
  'Create a sticky note on a Miro board',
  {
    board_id: z.string().describe('The Miro board ID'),
    content: z.string().describe('Text content of the sticky note'),
    x: z.number().optional().describe('X position (default 0)'),
    y: z.number().optional().describe('Y position (default 0)'),
    color: z
      .enum(['gray', 'light_yellow', 'yellow', 'orange', 'light_green', 'green', 'dark_green', 'cyan', 'light_pink', 'pink', 'violet', 'red', 'light_blue', 'blue', 'dark_blue', 'black'])
      .optional()
      .describe('Sticky note color (default yellow)'),
  },
  async ({ board_id, content, x, y, color }) => {
    const note = await miro.createStickyNote(board_id, content, {
      x: x || 0,
      y: y || 0,
      color: color || 'yellow',
    });
    return {
      content: [{ type: 'text', text: `Sticky note created (id: ${note.id}) at (${note.position.x}, ${note.position.y})` }],
    };
  },
);

// === Shapes ===

server.tool(
  'miro_create_shape',
  'Create a shape (rectangle, circle, diamond, etc.) on a Miro board',
  {
    board_id: z.string().describe('The Miro board ID'),
    content: z.string().describe('Text inside the shape'),
    shape: z
      .enum(['rectangle', 'round_rectangle', 'circle', 'triangle', 'rhombus', 'parallelogram', 'trapezoid', 'pentagon', 'hexagon', 'octagon', 'wedge_round_rectangle_callout', 'star', 'flow_chart_predefined_process', 'cloud', 'cross', 'can', 'right_arrow', 'left_arrow', 'left_right_arrow', 'left_brace', 'right_brace'])
      .optional()
      .describe('Shape type (default rectangle)'),
    x: z.number().optional().describe('X position (default 0)'),
    y: z.number().optional().describe('Y position (default 0)'),
    width: z.number().optional().describe('Width in pixels (default 200)'),
    height: z.number().optional().describe('Height in pixels (default 100)'),
    fill_color: z.string().optional().describe('Fill color hex (default #FFFFFF)'),
    border_color: z.string().optional().describe('Border color hex (default #000000)'),
    font_size: z.string().optional().describe('Font size (default 14)'),
  },
  async ({ board_id, content, shape, x, y, width, height, fill_color, border_color, font_size }) => {
    const item = await miro.createShape(board_id, content, {
      shape: shape || 'rectangle',
      x: x || 0,
      y: y || 0,
      width: width || 200,
      height: height || 100,
      fillColor: fill_color || '#FFFFFF',
      borderColor: border_color || '#000000',
      fontSize: font_size || '14',
    });
    return {
      content: [{ type: 'text', text: `Shape "${content}" created (id: ${item.id}) at (${item.position.x}, ${item.position.y})` }],
    };
  },
);

// === Connectors ===

server.tool(
  'miro_create_connector',
  'Create a connector (line/arrow) between two items on a Miro board',
  {
    board_id: z.string().describe('The Miro board ID'),
    start_item_id: z.string().describe('ID of the starting item'),
    end_item_id: z.string().describe('ID of the ending item'),
    style: z.enum(['straight', 'elbowed', 'curved']).optional().describe('Connector style (default straight)'),
    label: z.string().optional().describe('Text label on the connector'),
  },
  async ({ board_id, start_item_id, end_item_id, style, label }) => {
    const connector = await miro.createConnector(board_id, start_item_id, end_item_id, {
      style: style || 'straight',
      label: label || '',
    });
    return {
      content: [{ type: 'text', text: `Connector created (id: ${connector.id}): ${start_item_id} → ${end_item_id}` }],
    };
  },
);

// === Text ===

server.tool(
  'miro_create_text',
  'Create a text element on a Miro board',
  {
    board_id: z.string().describe('The Miro board ID'),
    content: z.string().describe('Text content (supports basic HTML: <b>, <i>, <br>)'),
    x: z.number().optional().describe('X position (default 0)'),
    y: z.number().optional().describe('Y position (default 0)'),
    width: z.number().optional().describe('Width in pixels (default 300)'),
    font_size: z.string().optional().describe('Font size (default 14)'),
  },
  async ({ board_id, content, x, y, width, font_size }) => {
    const item = await miro.createText(board_id, content, {
      x: x || 0,
      y: y || 0,
      width: width || 300,
      fontSize: font_size || '14',
    });
    return {
      content: [{ type: 'text', text: `Text created (id: ${item.id}) at (${item.position.x}, ${item.position.y})` }],
    };
  },
);

// === Cards ===

server.tool(
  'miro_create_card',
  'Create a card (with title and description) on a Miro board',
  {
    board_id: z.string().describe('The Miro board ID'),
    title: z.string().describe('Card title'),
    description: z.string().optional().describe('Card description'),
    x: z.number().optional().describe('X position (default 0)'),
    y: z.number().optional().describe('Y position (default 0)'),
  },
  async ({ board_id, title, description, x, y }) => {
    const card = await miro.createCard(board_id, title, description || '', {
      x: x || 0,
      y: y || 0,
    });
    return {
      content: [{ type: 'text', text: `Card "${title}" created (id: ${card.id}) at (${card.position.x}, ${card.position.y})` }],
    };
  },
);

// === Frames ===

server.tool(
  'miro_create_frame',
  'Create a frame (grouping container) on a Miro board',
  {
    board_id: z.string().describe('The Miro board ID'),
    title: z.string().describe('Frame title'),
    x: z.number().optional().describe('X position (default 0)'),
    y: z.number().optional().describe('Y position (default 0)'),
    width: z.number().optional().describe('Width in pixels (default 800)'),
    height: z.number().optional().describe('Height in pixels (default 600)'),
    fill_color: z.string().optional().describe('Background color hex (default #F5F5F5)'),
  },
  async ({ board_id, title, x, y, width, height, fill_color }) => {
    const frame = await miro.createFrame(board_id, title, {
      x: x || 0,
      y: y || 0,
      width: width || 800,
      height: height || 600,
      fillColor: fill_color || '#F5F5F5',
    });
    return {
      content: [{ type: 'text', text: `Frame "${title}" created (id: ${frame.id}) at (${frame.position.x}, ${frame.position.y})` }],
    };
  },
);

// === Images ===

server.tool(
  'miro_create_image',
  'Add an image to a Miro board from a URL',
  {
    board_id: z.string().describe('The Miro board ID'),
    url: z.string().describe('Public URL of the image'),
    x: z.number().optional().describe('X position (default 0)'),
    y: z.number().optional().describe('Y position (default 0)'),
    width: z.number().optional().describe('Width in pixels (default 400)'),
  },
  async ({ board_id, url, x, y, width }) => {
    const image = await miro.createImageFromUrl(board_id, url, {
      x: x || 0,
      y: y || 0,
      width: width || 400,
    });
    return {
      content: [{ type: 'text', text: `Image created (id: ${image.id}) at (${image.position.x}, ${image.position.y})` }],
    };
  },
);

// === Start Server ===

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch((err) => {
  console.error('Server error:', err);
  process.exit(1);
});
