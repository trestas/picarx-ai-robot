#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
STAGE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "Collecting stage 03 artifacts from Raspberry Pi..."
scp "arvydas@PiCarX:/home/arvydas/stage3_picarx_base_hw/runtime_outputs/*" "$STAGE_DIR/artifacts/" 2>/dev/null || true
echo "Done."