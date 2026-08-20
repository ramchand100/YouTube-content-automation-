import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { theme } from "../theme";

interface EndCardProps {
  channelName: string;     // e.g. "Decode Pakistan"
  tagline?: string;        // e.g. "Business. Economics. Ground Truth."
  cta?: string;            // e.g. "Subscribe for new episodes every week"
  nextEpisode?: string;    // e.g. "Next: The Textile Export Engine"
}

export const EndCard: React.FC<EndCardProps> = ({
  channelName,
  tagline,
  cta,
  nextEpisode,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const bgOpacity = interpolate(frame, [0, fps * 0.4], [0, 1], { extrapolateRight: "clamp" });
  const nameOpacity = interpolate(frame, [fps * 0.3, fps * 0.7], [0, 1], { extrapolateRight: "clamp" });
  const nameSlide = interpolate(frame, [fps * 0.3, fps * 0.7], [24, 0], { extrapolateRight: "clamp" });
  const taglineOpacity = interpolate(frame, [fps * 0.6, fps * 0.9], [0, 1], { extrapolateRight: "clamp" });
  const ctaOpacity = interpolate(frame, [fps * 1.0, fps * 1.3], [0, 1], { extrapolateRight: "clamp" });
  const nextOpacity = interpolate(frame, [fps * 1.4, fps * 1.7], [0, 1], { extrapolateRight: "clamp" });

  const accentW = interpolate(frame, [fps * 0.4, fps * 0.8], [0, 100], { extrapolateRight: "clamp" });

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
        opacity: bgOpacity,
      }}
    >
      {/* Channel name */}
      <div
        style={{
          opacity: nameOpacity,
          transform: `translateY(${nameSlide}px)`,
          fontFamily: theme.fontTitle,
          fontSize: theme.headingSize,
          color: theme.text,
          letterSpacing: "-1px",
        }}
      >
        {channelName}
      </div>

      {/* Accent bar */}
      <div
        style={{
          width: accentW,
          height: 4,
          backgroundColor: theme.green,
          borderRadius: 2,
          marginTop: 20,
          marginBottom: 20,
        }}
      />

      {/* Tagline */}
      {tagline && (
        <div
          style={{
            opacity: taglineOpacity,
            fontFamily: theme.fontBody,
            fontSize: theme.bodySize,
            color: theme.textSecondary,
            letterSpacing: 2,
            textTransform: "uppercase",
            marginBottom: 48,
          }}
        >
          {tagline}
        </div>
      )}

      {/* CTA */}
      {cta && (
        <div
          style={{
            opacity: ctaOpacity,
            fontFamily: theme.fontBody,
            fontSize: theme.captionSize,
            color: theme.text,
            backgroundColor: theme.green,
            padding: "18px 48px",
            borderRadius: 8,
            color: "#FFFFFF",
            fontWeight: 600,
            marginBottom: nextEpisode ? 40 : 0,
          }}
        >
          {cta}
        </div>
      )}

      {/* Next episode */}
      {nextEpisode && (
        <div
          style={{
            opacity: nextOpacity,
            fontFamily: theme.fontBody,
            fontSize: theme.captionSize,
            color: theme.textSecondary,
          }}
        >
          {nextEpisode}
        </div>
      )}
    </div>
  );
};
