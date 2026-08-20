// Channel visual identity — white background style
export const theme = {
  // Canvas
  bg: "#F8F9FA",          // off-white background
  cardBg: "#FFFFFF",       // card fill
  cardShadow: "0 2px 12px rgba(0,0,0,0.08)",

  // Text
  text: "#1A1A1A",         // primary
  textSecondary: "#555555", // captions, labels
  textDim: "#999999",      // very secondary

  // Accents
  green: "#1EB53A",        // growth, viable, positive
  greenLight: "#E8F5EB",   // green tint background
  red: "#D32F2F",          // cost gap, risk, decline
  redLight: "#FDECEA",     // red tint background

  // Borders
  border: "#E0E0E0",
  borderStrong: "#BDBDBD",

  // Typography (loaded via Google Fonts in the HTML, referenced by name here)
  fontTitle: "'Archivo Black', sans-serif",
  fontBody: "'Inter', sans-serif",

  // Sizes (at 1920x1080)
  titleSize: 96,
  headingSize: 56,
  subheadingSize: 36,
  bodySize: 28,
  captionSize: 22,
  sourceCaptionSize: 18,
};

export const fps = 30;
export const width = 1920;
export const height = 1080;
