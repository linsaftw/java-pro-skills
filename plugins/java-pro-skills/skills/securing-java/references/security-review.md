# Security review map

Check:
- trust boundaries and authenticated identity source
- object/resource-level authorization
- injection sinks: SQL, shell, expression/template, log, headers
- path traversal/archive extraction
- SSRF/DNS rebinding/redirect policy
- parser and decompression limits
- unsafe deserialization/polymorphic JSON configuration
- cryptographic algorithm/key/nonce lifecycle
- secrets in config/logs/errors
- TLS hostname/certificate validation
- CORS/CSRF/session/cookie rules for web apps
- rate limits and abuse controls at expensive endpoints
- dependency provenance, SBOM/advisory evidence
