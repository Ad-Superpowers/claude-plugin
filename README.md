# Ad Superpowers for Claude

Manage, analyze, and optimize your ad campaigns across 8 platforms through natural language in Claude Code and Claude Desktop.

**120 expert skills** · **35 slash commands** (29 workflow, 6 utility) · **5 specialized agents** · **50 MCP tools**

## Platforms

| Platform | Skills | MCP Tools | What you can do |
|----------|-------:|----------:|------------------|
| **Meta Ads** | 26 | 14 | Campaign management, creative fatigue analysis, audience targeting, ad creation, budget optimization |
| **Google Ads** | 32 | 4 | GAQL queries, Performance Max, keyword strategy, bid optimization, campaign creation |
| **Google Analytics 4** | 18 | 2 | Event tracking, attribution models, audience building, ecommerce analysis |
| **Google Search Console** | 2 | 3 | SEO performance, keyword rankings, indexing diagnostics, sitemap management |
| **Google Tag Manager** | 4 | 4 | Container auditing, consent mode, server-side tagging, conversion setup |
| **Google Merchant Center** | 0 | 3 | Feed accounts, product issues, disapprovals ranked by click potential, shopping performance (read-only) |
| **LinkedIn Ads** | 11 | 5 | B2B lead gen, ABM targeting, revenue attribution, Thought Leader Ads, CTV |
| **TikTok Ads** | 10 | 9 | Creative fatigue, video performance, Smart+ campaigns, Search Ads, Shop |
| **Cross-platform** | 17 | 6 | Unified `workflow`, `skill`, `skill_update`, `workflow_update`, `clients`, and `clients_update` tools; client profiles, attribution reconciliation, SEO vs SEA gaps, budget allocation, competitive analysis |

## Install

Pick the path that matches how you use Claude. All four give you the MCP tools; only Claude Code and Cowork give you the bundled skills, commands, and agents.

### Claude Code (terminal or VSCode extension)

**Requires Claude Code `2.1.74` or newer.** Earlier versions had an upstream bug ([anthropics/claude-code#21560](https://github.com/anthropics/claude-code/issues/21560)) that prevented plugin-defined subagents from accessing MCP tools; it is fixed in 2.1.74+. Upgrade with `npm i -g @anthropic-ai/claude-code@latest` (terminal) or via the VSCode extension marketplace, then `Developer: Reload Window`.

Add the marketplace once, then install the plugin:

```bash
/plugin marketplace add Ad-Superpowers/ad-superpowers-plugin
/plugin install ad-superpowers@ad-superpowers
```

That's it. The MCP server, all 120 skills, 35 slash commands, 5 agents, and safety confirmations are bundled.

### Cowork (Claude Desktop's agentic coding mode)

Cowork supports plugins through an admin UI, not through a slash command. This path is available on **Team** and **Enterprise** plans, and only Owners or Primary Owners can add plugins for the organization.

1. In Claude Desktop, go to **Organization settings → Plugins**
2. Click **Add plugin** and choose **Sync from GitHub**
3. Enter the repository: `Ad-Superpowers/ad-superpowers-plugin`
4. Set distribution: **Available for install** (members can opt in) or **Installed by default**
5. Members then open **Browse plugins** inside Cowork to install it

Once installed, members get the skills, commands, and MCP tools inside Cowork. The 5 bundled subagents do not currently launch in Cowork — see [Known limitations](#known-limitations) below for details and the Skill-based workarounds.

### Claude Desktop (chat mode, via Connectors)

The regular Claude Desktop chat interface doesn't have a plugin system. You can still get the MCP tools by adding Ad Superpowers as a Connector, but you won't get the bundled skills, commands, or agents (those need Claude Code or Cowork).

1. Open Claude Desktop
2. Go to **Settings → Connectors → Add Custom Connector**
3. Enter the URL: `https://mcp.adsuperpowers.ai/v1`
4. Complete the OAuth flow in your browser

If you want the full experience, use Claude Code or Cowork instead.

### ChatGPT

ChatGPT can reach the Ad Superpowers MCP server as a custom connector. You'll get the MCP tools but not the bundled skills, commands, or agents.

1. Open ChatGPT settings and go to connectors
2. Add a custom connector pointing at `https://mcp.adsuperpowers.ai/v1`
3. Complete the OAuth flow in your browser

Whether custom connectors are available to you depends on your ChatGPT plan.

## Setup

1. Create an account at [app.adsuperpowers.ai](https://app.adsuperpowers.ai)
2. Connect your ad platforms through OAuth in the dashboard
3. Start asking Claude about your campaigns

No API keys to configure, no manual MCP setup. Authentication happens via OAuth through the Ad Superpowers dashboard.

## What you can do

### Ask questions in natural language

* "How are my Meta campaigns performing this week?"
* "Which Google Ads keywords have the highest CPA?"
* "Compare my LinkedIn and Meta lead gen performance"
* "Is my TikTok creative showing signs of fatigue?"
* "What's my organic vs paid keyword overlap?"

### Run workflow commands

| Command | What it does |
|---------|--------------|
| `/ad-superpowers:weekly-performance-pulse` | Cross-platform weekly health check |
| `/ad-superpowers:creative-fatigue-scanner` | Detect fatigued creatives across platforms |
| `/ad-superpowers:budget-allocation-planner` | Data-driven budget reallocation recommendations |
| `/ad-superpowers:keyword-opportunities` | SEO vs paid keyword gap analysis |
| `/ad-superpowers:monthly-executive-summary` | Executive-ready monthly performance report |
| `/ad-superpowers:anomaly-detective` | Detect performance anomalies across campaigns |
| `/ad-superpowers:competitive-landscape-analyzer` | Competitive positioning analysis |

[See all 35 commands](plugin/commands/)

### Specialized agents

Claude automatically delegates to the right agent based on your task:

| Agent | Focus | Triggers |
|-------|-------|----------|
| **marketing-strategist** | Strategy, competitive analysis, channel selection, personas | "analyze competition", "which channels?", "new client onboarding" |
| **media-buyer** | Campaign execution, budgets, bidding, audiences, scaling | "create campaign", "optimize budget", "scale winners" |
| **creative-analyst** | Creative fatigue detection, A/B tests, refresh strategy | "check creative fatigue", "which ads are tired" |
| **reporting-agent** | Structured performance reports and comparisons | "weekly report", "monthly summary" |
| **tracking-specialist** | GTM audits, conversion tracking, SEO vs SEA analysis | "audit my GTM", "keyword overlap", "missing conversions" |

### Expert skills (auto-invoked)

Claude automatically uses the right skill based on your question. Skills provide decision frameworks, benchmarks, and actionable recommendations for:

* Campaign optimization (bid strategies, budget scaling, learning phase management)
* Creative analysis (fatigue detection, A/B testing, diversification)
* Audience strategy (lookalike planning, overlap detection, remarketing)
* Measurement (attribution models, conversion tracking, CAPI setup)
* Technical work (GAQL queries, GTM auditing, GA4 event tracking)

### Write operations (with safety)

* Create Meta ads (image upload, creative, and ad in one step)
* Duplicate ads with creative overrides
* Pause or resume campaigns and update budgets
* Create Google Ads campaigns (budget, campaign, ad group, ads, keywords)

All write operations include safety confirmations:

* Campaigns always create paused so you can review before going live
* Budget changes require explicit approval
* Destructive operations are clearly flagged

## Known limitations

### Bundled subagents do not launch in Cowork (Claude Desktop agentic mode)

The 5 bundled agents (`marketing-strategist`, `media-buyer`, `creative-analyst`, `reporting-agent`, `tracking-specialist`) launch correctly in **Claude Code** (terminal and VSCode extension, 2.1.74+). They do **not** currently launch in **Cowork**, the agentic coding mode inside Claude Desktop.

**What's happening:** When the plugin is installed in a Cowork session, Cowork's plugin loader reads the plugin's skills, commands, and MCP server correctly, but it does not register the markdown files in `agents/` with the Agent tool's `subagent_type` registry. The Agent tool in Cowork still only exposes its five built-in subagents (`general-purpose`, `Explore`, `Plan`, `statusline-setup`, `claude-code-guide`). Attempting `Agent(subagent_type="creative-analyst", ...)` returns "agent type not found." Our agent files validate cleanly against the [plugin spec](https://code.claude.com/docs/en/plugins-reference#agents), so this is a Cowork harness limitation, not a plugin defect.

This is consistent with other known Cowork plugin-loading issues tracked upstream ([#39274](https://github.com/anthropics/claude-code/issues/39274), [#40774](https://github.com/anthropics/claude-code/issues/40774)), and there is currently no plugin-author-side opt-in, whitelist, or setting that changes this behavior. We have filed a request with Anthropic to expose plugin-bundled agents through Cowork's Agent tool.

**What works in Cowork today:** Everything except `Agent()` dispatch.

* All 120 skills load and auto-invoke on relevant questions
* All 35 slash commands are discoverable and runnable
* MCP tools are callable from the main conversation, exactly as in any other client
* All write operations (create campaign, duplicate ad, update budget) work
* The agents' **prompts and logic** are also available as slash commands and skills — you get the same analysis, it just runs in the main context window instead of a separate subagent

So in practice, asking Claude directly in Cowork — *"run a creative fatigue scan on my Meta account"* or *"write a weekly performance report"* — gives you the same deliverable the subagent would have produced. It loads the relevant skill (`meta-creative-fatigue-analyzer`, `weekly-performance-pulse`, etc.) and calls the MCP tools directly in the main thread.

### Claude Code (terminal and VSCode)

No known limitations on 2.1.74+. All skills, commands, MCP tools, and subagents work as documented. Earlier versions had [#21560](https://github.com/anthropics/claude-code/issues/21560) (subagents couldn't access plugin MCP tools); that is fixed.

### Host compatibility matrix

| Component | Claude Code CLI / VSCode | Cowork (Claude Desktop) | Claude Desktop (chat, via Connector) | ChatGPT (via Connector) |
|-----------|:---:|:---:|:---:|:---:|
| 120 skills | ✅ | ✅ | ❌ | ❌ |
| 35 commands | ✅ | ✅ | ❌ | ❌ |
| 50 MCP tools | ✅ | ✅ | ✅ | ✅ |
| 5 subagents | ✅ | ❌ (use skills instead) | ❌ | ❌ |

## Paid early access

| Tier | Monthly | Annual | Tool calls/mo | Accounts | Users | Platforms |
|------|--------:|-------:|--------------:|---------:|------:|-----------|
| **Pro** | €99 | €79 | 1,500 | 25 | 1 | All 8 |
| **Team** | €249 | €199 | 6,000 | 100 | 5 | All 8 |

Each organization can use one 14-day Pro or Team trial, capped at 200 tool calls. Trial requires a credit card and converts to the selected plan after 14 days unless cancelled. Annual plans get a 20% discount. A "tool call" is one MCP tool invocation; workflows that fan out to multiple tools count each invocation. Enterprise enquiries use custom usage and volume pricing. Start at [adsuperpowers.ai](https://adsuperpowers.ai).

## Security

* OAuth authentication; platform credentials are held encrypted on our server, not on your machine
* All API communication over HTTPS
* Users can revoke platform access at any time
* Per-user authentication in team environments
* See [SECURITY.md](SECURITY.md) for our responsible disclosure policy

## Support

* Website: [adsuperpowers.ai](https://adsuperpowers.ai)
* Dashboard: [app.adsuperpowers.ai](https://app.adsuperpowers.ai)
* Email: contact@adsuperpowers.ai

## License

MIT, see [LICENSE](LICENSE)
