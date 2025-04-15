# Integration Limitations with Granary and Tweepy (Twitter, Facebook, Instagram)

## Overview
This document records technical and scientific limitations found during the integration of social media platforms using the Granary and Tweepy Python libraries. It supports reproducibility and transparency for the MHAI research project.

---

## Twitter (X) API Limitations

### ✅ Using Tweepy:
- Twitter (now X) requires **paid developer accounts** (as of mid-2023).
- Many endpoints now return `403 Forbidden` or `401 Unauthorized` without elevated access.
- Errors encountered:
  - `tweepy.errors.Unauthorized: 401 Unauthorized`
  - `403 Too Many Requests`
- v2 endpoints like `get_users_tweets` are still accessible with Bearer Tokens.

### 🛑 Using Granary:
- Internally uses Twitter API v1.1 endpoints (e.g. `/search/tweets.json`) which now require elevated or paid access.
- Even with OAuth 1.0a tokens, access results in:
  - `403 Forbidden`
  - `OAuthError: Only a subset of v1.1 endpoints is available`
- The Granary maintainer has acknowledged these limitations:
  - [Granary Issue #197](https://github.com/snarfed/granary/issues/197)

### ⚠️ Tracebacks:

> granary.source.ApiError: Twitter API returned 403 Forbidden
> ValueError: Only unicode objects are escapable. Got None of type <class 'NoneType'>
> ScraperException: SSLCertVerificationError when using snscrape

### Notes:
- Twitter’s increasing paywall is incompatible with open science principles.
- Reproducibility in studies using social media content is severely impacted.

---

## Facebook & Instagram (Graph API)

### ❌ Granary:
- Does **not** support Facebook or Instagram at all.

### ⚠️ Facebook Graph API:
- Requires:
  - App approval
  - OAuth access
  - `user_posts` permission (hard to get)
- Even with tokens, many requests fail unless the app is fully verified.

### ⚠️ Instagram Graph API:
- Only available for:
  - **Business** or **Creator** accounts
  - Managed via **Facebook Business Manager**
- API is **not usable for personal user feeds**.
- Requires connection to a Facebook Page.
- Requires elevated permissions and app review.

### Tracebacks:
> OAuthException: (#10) Application does not have permission for this action
: RuntimeError: Facebook API error: An active access token must be used to query information

---

## Tools and Libraries Investigated

| Tool | Purpose | Outcome |
|------|---------|---------|
| `granary` | Unified API for social feeds | ⚠️ Broken Twitter support, no Instagram/Facebook |
| `tweepy` | Twitter API wrapper | ⚠️ Requires paid tier for many endpoints |
| `snscrape` | Public scraping | ❌ Blocked by Twitter certificate / API changes |
| `requests` + Graph API | Facebook / Instagram | ⚠️ Manual token setup; limited user access |

---

## References

- [Twitter API Docs](https://developer.twitter.com/en/docs)
- [Granary GitHub](https://github.com/snarfed/granary/issues)
- [Tweepy Docs](https://docs.tweepy.org/en/stable/)
- [Facebook Graph API](https://developers.facebook.com/docs/graph-api/)
- [Instagram API](https://developers.facebook.com/docs/instagram-api)
