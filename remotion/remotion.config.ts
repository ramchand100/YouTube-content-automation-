import {Config} from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
// If Remotion cannot download its own Chrome Headless Shell in this environment,
// point it at the pre-installed browser instead (see remotion/README.md):
// Config.setBrowserExecutable('/opt/pw-browsers/chromium');
