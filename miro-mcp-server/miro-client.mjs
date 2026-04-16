const BASE_URL = 'https://api.miro.com/v2';

export class MiroClient {
  constructor(token) {
    if (!token) throw new Error('MIRO_API_TOKEN is required');
    this.token = token;
  }

  async request(method, path, body = null) {
    const url = `${BASE_URL}${path}`;
    const options = {
      method,
      headers: {
        'Authorization': `Bearer ${this.token}`,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
    };
    if (body) options.body = JSON.stringify(body);

    const res = await fetch(url, options);
    const text = await res.text();

    if (!res.ok) {
      throw new Error(`Miro API ${method} ${path} failed (${res.status}): ${text}`);
    }

    return text ? JSON.parse(text) : null;
  }

  // === Boards ===

  async listBoards() {
    return this.request('GET', '/boards');
  }

  async getBoard(boardId) {
    return this.request('GET', `/boards/${boardId}`);
  }

  async createBoard(name, description = '') {
    return this.request('POST', '/boards', { name, description });
  }

  // === Items (read) ===

  async getBoardItems(boardId, limit = 50, cursor = '') {
    const params = new URLSearchParams({ limit: String(limit) });
    if (cursor) params.set('cursor', cursor);
    return this.request('GET', `/boards/${boardId}/items?${params}`);
  }

  // === Sticky Notes ===

  async createStickyNote(boardId, content, { x = 0, y = 0, width = 199, color = 'yellow' } = {}) {
    return this.request('POST', `/boards/${boardId}/sticky_notes`, {
      data: { content, shape: 'square' },
      style: { fillColor: color },
      position: { x, y },
      geometry: { width },
    });
  }

  // === Shapes ===

  async createShape(boardId, content, { x = 0, y = 0, width = 200, height = 100, shape = 'rectangle', fillColor = '#FFFFFF', borderColor = '#000000', fontSize = '14' } = {}) {
    return this.request('POST', `/boards/${boardId}/shapes`, {
      data: { content, shape },
      style: {
        fillColor,
        borderColor,
        borderWidth: '2.0',
        fontFamily: 'arial',
        fontSize,
        textAlign: 'center',
        textAlignVertical: 'middle',
      },
      position: { x, y },
      geometry: { width, height },
    });
  }

  // === Connectors ===

  async createConnector(boardId, startItemId, endItemId, { style = 'straight', label = '' } = {}) {
    const body = {
      startItem: { id: startItemId },
      endItem: { id: endItemId },
      style: { strokeStyle: 'normal', strokeWidth: '2.0' },
      shape: style,
    };
    if (label) {
      body.captions = [{ content: label, position: '50%' }];
    }
    return this.request('POST', `/boards/${boardId}/connectors`, body);
  }

  // === Text ===

  async createText(boardId, content, { x = 0, y = 0, width = 300, fontSize = '14' } = {}) {
    return this.request('POST', `/boards/${boardId}/texts`, {
      data: { content },
      style: { fontSize, fontFamily: 'arial' },
      position: { x, y },
      geometry: { width },
    });
  }

  // === Cards ===

  async createCard(boardId, title, description = '', { x = 0, y = 0, width = 320 } = {}) {
    return this.request('POST', `/boards/${boardId}/cards`, {
      data: { title, description },
      position: { x, y },
      geometry: { width },
    });
  }

  // === Frames ===

  async createFrame(boardId, title, { x = 0, y = 0, width = 800, height = 600, fillColor = '#F5F5F5' } = {}) {
    return this.request('POST', `/boards/${boardId}/frames`, {
      data: { title, format: 'custom', type: 'freeform' },
      style: { fillColor },
      position: { x, y },
      geometry: { width, height },
    });
  }

  // === Images ===

  async createImageFromUrl(boardId, url, { x = 0, y = 0, width = 400 } = {}) {
    return this.request('POST', `/boards/${boardId}/images`, {
      data: { url },
      position: { x, y },
      geometry: { width },
    });
  }
}
