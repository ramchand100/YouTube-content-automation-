import { useCurrentFrame, useVideoConfig, interpolate, spring } from "remotion";
import { theme } from "../theme";

interface DefCardProps {
  term: string;
  definition: string;
  sourceCaption?: string;
  accentColor?: string; // defaults to theme.green
}

export const DefCard: React.FC<DefCardProps> = ({
  term,
  definition,
  sourceCaption,
  accentColor = theme.green,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const containerOpacity = interpolate(frame, [0, fps * 0.4], [0, 1], {
    extrapolateRight: "clamp",
  });

  const slideY = interpolate(frame, [0, fps * 0.4], [24, 0], {
    extrapolateRight: "clamp",
  });

  const definitionOpacity = interpolate(
    frame,
    [fps * 0.5, fps * 0.9],
    [0, 1],
    { extrapolateRight: "clamp" }
  );

  const sourceOpacity = interpolate(
    frame,
    [fps * 1.0, fps * 1.3],
    [0, 1],
    { extrapolateRight: "clamp" }
  );

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        backgroundColor: theme.bg,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: theme.fontBody,
      }}
    >
      <div
        style={{
          opacity: containerOpacity,
          transform: `translateY(${slideY}px)`,
          backgroundColor: theme.cardBg,
          boxShadow: theme.cardShadow,
          borderRadius: 16,
          borderLeft: `8px solid ${accentColor}`,
          padding: "64px 80px",
          maxWidth: 1200,
          width: "80%",
        }}
      >
        {/* Term */}
        <div
          style={{
            fontFamily: theme.fontTitle,
            fontSize: theme.headingSize,
            color: accentColor,
            letterSpacing: "-1px",
            marginBottom: 16,
          }}
        >
          {term}
        </div>

        {/* Separator */}
        <div
          style={{
            width: 60,
            height: 4,
            backgroundColor: accentColor,
            borderRadius: 2,
            marginBottom: 32,
          }}
        />

        {/* Definition */}
        <div
          style={{
            opacity: definitionOpacity,
            fontFamily: theme.fontBody,
            fontSize: theme.bodySize,
            color: theme.text,
            lineHeight: 1.6,
          }}
        >
          {definition}
        </div>

        {/* Source caption */}
        {sourceCaption && (
          <div
            style={{
              opacity: sourceOpacity,
              marginTop: 40,
              fontFamily: theme.fontBody,
              fontSize: theme.sourceCaptionSize,
              color: theme.textSecondary,
            }}
          >
            {sourceCaption}
          </div>
        )}
      </div>
    </div>
  );
};
