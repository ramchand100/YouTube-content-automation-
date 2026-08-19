// Channel palette and type, shared across all scenes.
// Mirrors CLAUDE.md / the storyboards: black base, white text, green = positive /
// "free" / stays-home, red = fee / cost / leakage.

export const theme = {
  bg: '#0A0A0A',
  surface: '#151515',
  border: '#262626',
  text: '#F5F5F5',
  muted: '#9CA3AF',
  green: '#1EB53A', // Raast / free / value kept
  red: '#FB5A5A', // fees / cost / leakage
  // Load Coolvetica/Archivo Black via @remotion/google-fonts or @remotion/fonts for
  // production. Falls back to a bold system stack until then (see README).
  display:
    "'Archivo Black', 'Coolvetica', 'Arial Black', system-ui, sans-serif",
  body: "Inter, system-ui, -apple-system, sans-serif",
};

// Format an integer as PKR, e.g. 2000 -> "Rs 2,000".
export const pkr = (n: number): string =>
  'Rs ' + Math.round(n).toLocaleString('en-US');
