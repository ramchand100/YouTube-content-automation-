import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { theme } from "../theme";

interface StatItem {
  label: string;
  value: string;
  color?: string; // theme.green or theme.red
}

interface OpeningStatsProps {
  left: StatItem;
  right: StatItem;
  contrastLine?: string;   // e.g. "7× MORE EXPENSIVE"
  sourceCaption?: string;
}

export const OpeningStats: React.FC<OpeningStatsProps> = ({
  left,
  right,
  contrastLine,
  sourceCaption,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const leftOpacity = interpolate(frame, [0, fps * 0.4], [0, 1], { extrapolateRight: "clamp" });
  const rightOpacity = interpolate(frame, [fps * 0.6, fps * 1.0], [0, 1], { extrapolateRight: "clamp" });
  const contrastOpacity = interpolate(frame, [fps * 1.2, fps * 1.5], [0, 1], { extrapolateRight: "clamp" });
  const sourceOpacity = interpolate(frame, [fps * 1.6, fps * 1.9], [0, 1], { extrapolateRight: "clamp" });

  const leftSlide = interpolate(frame, [0, fps * 0.4], [-40, 0], { extrapolateRight: "clamp" });
  const rightSlide = interpolate(frame, [fps * 0.6, fps * 1.0], [40, 0], { extrapolateRight: "clamp" });

  const leftColor = left.color ?? theme.green;
  const rightColor = right.color ?? theme.red;

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        backgroundColor: theme.bg,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: theme.fontBody,
        gap: 0,
      }}
    >
      {/* Two stats side by side */}
      <div style={{ display: "flex", alignItems: "stretch", gap: 0, width: "80%", maxWidth: 1400 }}>
        {/* LEFT */}
        <div
          style={{
            flex: 1,
            opacity: leftOpacity,
            transform: `translateX(${leftSlide}px)`,
            backgroundColor: theme.cardBg,
            boxShadow: theme.cardShadow,
            borderRadius: "16px 0 0 16px",
            borderTop: `6px solid ${leftColor}`,
            padding: "60px 64px",
            display: "flex",
            flexDirection: "column",
            gap: 16,
          }}
        >
          <div style={{ fontFamily: theme.fontBody, fontSize: theme.captionSize, color: theme.textSecondary, textTransform: "uppercase", letterSpacing: 2 }}>
            {left.label}
          </div>
          <div style={{ fontFamily: theme.fontTitle, fontSize: theme.titleSize, color: leftColor, lineHeight: 1 }}>
            {left.value}
          </div>
        </div>

        {/* Vertical divider */}
        <div style={{ width: 2, backgroundColor: theme.border }} />

        {/* RIGHT */}
        <div
          style={{
            flex: 1,
            opacity: rightOpacity,
            transform: `translateX(${rightSlide}px)`,
            backgroundColor: theme.cardBg,
            boxShadow: theme.cardShadow,
            borderRadius: "0 16px 16px 0",
            borderTop: `6px solid ${rightColor}`,
            padding: "60px 64px",
            display: "flex",
            flexDirection: "column",
            gap: 16,
          }}
        >
          <div style={{ fontFamily: theme.fontBody, fontSize: theme.captionSize, color: theme.textSecondary, textTransform: "uppercase", letterSpacing: 2 }}>
            {right.label}
          </div>
          <div style={{ fontFamily: theme.fontTitle, fontSize: theme.titleSize, color: rightColor, lineHeight: 1 }}>
            {right.value}
          </div>
        </div>
      </div>

      {/* Contrast line */}
      {contrastLine && (
        <div
          style={{
            opacity: contrastOpacity,
            marginTop: 40,
            backgroundColor: theme.cardBg,
            boxShadow: theme.cardShadow,
            borderRadius: 12,
            padding: "20px 48px",
            fontFamily: theme.fontTitle,
            fontSize: theme.subheadingSize,
            color: theme.text,
            letterSpacing: "-0.5px",
          }}
        >
          {contrastLine}
        </div>
      )}

      {/* Source caption */}
      {sourceCaption && (
        <div
          style={{
            opacity: sourceOpacity,
            position: "absolute",
            bottom: 40,
            right: 60,
            fontFamily: theme.fontBody,
            fontSize: theme.sourceCaptionSize,
            color: theme.textSecondary,
          }}
        >
          {sourceCaption}
        </div>
      )}
    </div>
  );
};
