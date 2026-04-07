#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
STAGE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_ROOT="$(cd "$STAGE_DIR/../.." && pwd)"

source "$STAGE_DIR/configs/picarx_base.env"

echo "Deploying Stage 03 to ${ROBOT_USER}@${ROBOT_HOST}:${REMOTE_STAGE_DIR}"

ssh "${ROBOT_USER}@${ROBOT_HOST}" "mkdir -p ${REMOTE_STAGE_DIR}"
scp -r "$STAGE_DIR"/scripts "$STAGE_DIR"/configs "$STAGE_DIR"/src "${ROBOT_USER}@${ROBOT_HOST}:${REMOTE_STAGE_DIR}/"

echo "Deployment complete."