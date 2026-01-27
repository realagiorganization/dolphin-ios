# DEVPLAN

## Goals
- Maintain a stable iOS/iPadOS port of Dolphin with reproducible builds and release artifacts.
- Keep core emulator changes aligned with upstream Dolphin where feasible.
- Provide CI automation for build, BDD validation, and release distribution.

## Development Steps
1. Clone the repository and initialize submodules.
2. Install build dependencies (Xcode + Homebrew tools).
3. Configure the iOS bundle identifier and team ID in the Xcode configs.
4. Build locally with Xcode or scripted build steps.
5. Update iOS-specific code and assets under `Source/iOS`.
6. Run the BDD validation suite for key user journeys.
7. Validate packaging outputs (IPA, TIPA, DEB) before release.
8. Cut a release and let CI upload to TestFlight.

## External Dependencies
- macOS (Big Sur 11.3+) and Xcode 13+ with iOS SDKs for building iOS targets.
- Homebrew packages: `cmake`, `ninja`, `bartycrouch`, `dpkg` (packaging).
- Python 3 for automation scripts and CI validation.
- Git submodules for bundled libraries in `Externals/` (FFmpeg, etc.).
- Apple Developer Program credentials for signing and TestFlight distribution.
- App Store Connect API keys for automated TestFlight uploads.
- Firebase (GoogleService-Info.plist) for analytics/crash reporting.
- Self-hosted macOS runner for GitHub Actions builds.
- Playwright (CI-only) for GitHub Pages screenshot capture.

## CI/Automation
- Build workflow: archives, IPAs, and DEBs on self-hosted macOS runners.
- Release workflow: builds release artifacts, creates GitHub release, uploads to TestFlight.
- BDD workflow: validates Gherkin feature files.
- VHS workflow: records console demo GIF for README.
- Website screenshot workflow: captures GitHub Pages preview on demand.
