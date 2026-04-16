// storage.js — FAQ Chatbot data layer
// All reads and writes to localStorage go through these functions.

const STORAGE_KEY = 'faq_config';

const SEED_DATA = {
  settings: {
    widgetTitle: { en: 'FAQ', ja: 'よくある質問' },
    welcomeMessage: { en: 'How can we help you today?', ja: 'ご質問をお選びください。' },
    theme: '#005A9C',
    fallbackMode: 'both',
    fallbackPhone: '0120-XXX-XXX',
    fallbackEmail: 'support@example.com',
    supportedLanguages: [
      { code: 'en', label: 'English' },
      { code: 'ja', label: '日本語' }
    ]
  },
  categories: [
    {
      id: 'cat_reimbursement',
      label: { en: 'Reimbursement', ja: '保険適用' },
      faqs: [
        {
          id: 'q_reimb_1',
          source: 'en',
          question: {
            en: 'What are the reimbursement criteria?',
            ja: '保険適用の基準は何ですか？'
          },
          answer: {
            en: 'Reimbursement is available for patients who meet the following criteria: confirmed diagnosis, prior authorization from a specialist, and prescription from a licensed physician.',
            ja: '以下の基準を満たす患者に保険が適用されます：確定診断、専門医による事前承認、および認定医師による処方。'
          }
        },
        {
          id: 'q_reimb_2',
          source: 'en',
          question: {
            en: 'How do I submit a reimbursement claim?',
            ja: '保険請求はどのように申請しますか？'
          },
          answer: {
            en: 'Submit the completed claim form along with supporting documentation to your regional insurance office within 30 days of treatment.',
            ja: '治療から30日以内に、必要書類とともに記入済みの申請書を地域の保険事務所に提出してください。'
          }
        },
        {
          id: 'q_reimb_3',
          source: 'en',
          question: {
            en: 'Which insurance plans are covered?',
            ja: 'どの保険プランが対象ですか？'
          },
          answer: {
            en: 'This product is covered under National Health Insurance (NHI) and most supplemental insurance plans. Please confirm with your specific insurer.',
            ja: 'この製品は国民健康保険および多くの補足保険プランの対象です。具体的な保険会社にご確認ください。'
          }
        }
      ]
    },
    {
      id: 'cat_prescription',
      label: { en: 'Prescription', ja: '処方' },
      faqs: [
        {
          id: 'q_presc_1',
          source: 'en',
          question: {
            en: 'Who can prescribe this medication?',
            ja: 'この薬を処方できるのは誰ですか？'
          },
          answer: {
            en: 'This medication must be prescribed by a licensed physician with appropriate specialist qualifications. General practitioners may prescribe with specialist consultation.',
            ja: 'この薬は適切な専門資格を持つ認定医師が処方する必要があります。一般開業医は専門医との相談のうえ処方することができます。'
          }
        },
        {
          id: 'q_presc_2',
          source: 'en',
          question: {
            en: 'What is the recommended dosage?',
            ja: '推奨用量は何ですか？'
          },
          answer: {
            en: 'Dosage should be determined by the prescribing physician based on the patient\'s individual clinical profile. Please refer to the approved prescribing information.',
            ja: '用量は処方医が患者の個別の臨床プロファイルに基づいて決定する必要があります。承認された処方情報を参照してください。'
          }
        },
        {
          id: 'q_presc_3',
          source: 'en',
          question: {
            en: 'Are there any contraindications?',
            ja: '禁忌事項はありますか？'
          },
          answer: {
            en: 'Yes, contraindications include hypersensitivity to the active substance and concurrent use of certain medications. Please review the full prescribing information for a complete list.',
            ja: 'はい、禁忌には活性物質に対する過敏症および特定の薬との併用が含まれます。完全なリストについては処方情報全文をご確認ください。'
          }
        }
      ]
    }
  ]
};

function loadConfig() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) {
    saveConfig(SEED_DATA);
    return SEED_DATA;
  }
  return JSON.parse(raw);
}

function saveConfig(config) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(config));
}

function getText(obj, lang) {
  if (typeof obj === 'string') return obj;
  return obj[lang] || obj['en'] || Object.values(obj)[0] || '';
}
