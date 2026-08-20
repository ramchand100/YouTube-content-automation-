import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { theme } from "../theme";

interface TitleCardProps {
  episodeNumber: string;  // e.g. "Episode 06"
  title: string;          // e.g. "The LNG Trap"
  subtitle?: string;      // e.g. "How Pakistan got hooked on expensive gas"
  pillar?: string;        // e.g. "MACRO · ENERGY"
}

export const TitleCard: React.FC<TitleCardProps> = ({
  episodeNumber,
  title,
  subtitle,
  pillar,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const pillarOpacity = interpolate(frame, [0, fps * 0.25], [0, 1], { extrapolateRight: "clamp" });
  const epOpacity = interpolate(frame, [fps * 0.15, fps * 0.4], [0, 1], { extrapolateRight: "clamp" });
  const titleOpacity = interpolate(frame, [fps * 0.35, fps * 0.75], [0, 1], { extrapolateRight: "clamp" });
  const titleSlide = interpolate(frame, [fps * 0.35, fps * 0.75], [32, 0], { extrapolateRight: "clamp" });
  const subtitleOpacity = interpolate(frame, [fps * 0.7, fps * 1.0], [0, 1], { extrapolateRight: "clamp" });

  const accentW = interpolate(frame, [fps * 0.3, fps * 0.7], [0, 120], { extrapolateRight: "clamp" });

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        backgroundColor: theme.bg,
        display: "flex",
        flexDirection: "column",
        alignItems: "flex-start",
        justifyContent: "center",
        fontFamily: theme.fontBody,
        padding: "80px 140px",
        boxSizing: "border-box",
      }}
    >
      {/* Pillar tag */}
      {pillar && (
        <div
          style={{
            opacity: pillarOpacity,
            fontFamily: theme.fontBody,
            fontSize: theme.captionSize,
            color: theme.green,
            textTransform: "uppercase",
            letterSpacing: 4,
            marginBottom: 24,
          }}
        >
          {pillar}
        </div>
      )}

      {/* Episode number */}
      <div
        style={{
          opacity: epOpacity,
          fontFamily: theme.fontBody,
          fontSize: theme.captionSize,
          color: theme.textSecondary,
          textTransform: "uppercase",
          letterSpacing: 3,
          marginBottom: 16,
        }}
      >
        {episodeNumber}
      </div>

      {/* Accent bar */}
      <div
        style={{
          width: accentW,
          height: 5,
          backgroundColor: theme.green,
          borderRadius: 3,
          marginBottom: 32,
        }}
      />

      {/* Main title */}
      <div
        style={{
          opacity: titleOpacity,
          transform: `translateY(${titleSlide}px)`,
          fontFamily: theme.fontTitle,
          fontSize: theme.titleSize,
          color: theme.text,
          lineHeight: 1.05,
          letterSpacing: "-2px",
          maxWidth: 1200,
        }}
      >
        {title}
      </div>

      {/* Subtitle */}
      {subtitle && (
        <div
          style={{
            opacity: subtitleOpacity,
            fontFamily: theme.fontBody,
            fontSize: theme.subheadingSize,
            color: theme.textSecondary,
            marginTop: 28,
            maxWidth: 1000,
            lineHeight: 1.4,
          }}
        >
          {subtitle}
        </div>
      )}
    </div>
  );
};
