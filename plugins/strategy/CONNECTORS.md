# Connectors

Some skills in this plugin (the ones adapted from Anthropic's knowledge-work-plugins) use `~~category` placeholders like `~~project tracker` or `~~chat`. A placeholder means "whatever tool you've connected in that category." Every skill also works without any connectors: just give Claude the context directly.

To connect tools, add connectors in your Claude settings (or configure MCP servers in Claude Code). Any tool with an MCP server in the right category works.

| Category | Placeholder | Common options |
|----------|-------------|----------------|
| Calendar | `~~calendar` | Google Calendar, Microsoft 365 |
| Chat | `~~chat` | Slack, Microsoft Teams |
| Competitive intelligence | `~~competitive intelligence` | Similarweb, Crayon, Klue |
| Design | `~~design` | Figma, Sketch, Adobe XD |
| Email | `~~email` | Gmail, Microsoft 365 |
| ITSM | `~~ITSM` | ServiceNow, Zendesk, Freshservice, Jira Service Management |
| Knowledge base | `~~knowledge base` | Notion, Confluence, Guru, Coda |
| Meeting transcription | `~~meeting transcription` | Fireflies, Gong, Dovetail, Otter.ai |
| Office suite | `~~office suite` | Microsoft 365, Google Workspace |
| Procurement | `~~procurement` | Coupa, SAP Ariba, Zip |
| Product analytics | `~~product analytics` | Amplitude, Pendo, Mixpanel, Heap, FullStory |
| Project tracker | `~~project tracker` | Linear, Asana, Jira, monday.com, ClickUp, Shortcut, Basecamp |
| User feedback | `~~user feedback` | Intercom, Productboard, Canny, UserVoice |

Adapted from the connector guides in Anthropic's [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache-2.0).
