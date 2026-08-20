import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { theme } from "../theme";

interface DominoBlock {
  label: string;
  color?: string; // defaults to theme.text; use theme.red for final/danger block
}

interface DominoChainProps {
  title?: string;
  blocks: DominoBlock[];
  sourceCaption?: string;
  defCard?: string;
}

export const DominoChain: React.FC<DominoChainProps> = ({
  title,
  blocks,
  sourceCaption,
  defCard,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleOpacity = interpolate(frame, [0, fps * 0.3], [0, 1], { extrapolateRight: "clamp" });

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
        padding: "60px 80px",
        boxSizing: "border-box",
      }}
    >
      {title && (
        <div
          style={{
            opacity: titleOpacity,
            fontFamily: theme.fontBody,
            fontSize: theme.captionSize,
            color: theme.textSecondary,
            textTransform: "uppercase",
            letterSpacing: 3,
            marginBottom: 56,
          }}
        >
          {title}
        </div>
      )}

      {/* Chain */}
      <div style={{ display: "flex", alignItems: "center", flexWrap: "wrap", gap: 0, justifyContent: "center", maxWidth: 1600 }}>
        {blocks.map((block, i) => {
          const delay = fps * (0.4 + i * 0.35);
          const blockOpacity = interpolate(frame, [delay, delay + fps * 0.3], [0, 1], { extrapolateRight: "clamp" });
          const blockScale = interpolate(frame, [delay, delay + fps * 0.3], [0.85, 1], { extrapolateRight: "clamp" });
          const arrowOpacity = interpolate(frame, [delay + fps * 0.2, delay + fps * 0.5], [0, 1], { extrapolateRight: "clamp" });
          const blockColor = block.color ?? theme.text;
          const isLast = i === blocks.length - 1;
          const isDanger = block.color === theme.red;

          return (
            <div key={i} style={{ display: "flex", alignItems: "center" }}>
              {/* Block */}
              <div
                style={{
                  opacity: blockOpacity,
                  transform: `scale(${blockScale})`,
                  backgroundColor: isDanger ? theme.redLight : theme.cardBg,
                  boxShadow: theme.cardShadow,
                  border: `2px solid ${isDanger ? theme.red : theme.border}`,
                  borderRadius: 12,
                  padding: "20px 28px",
                  fontFamily: theme.fontBody,
                  fontSize: theme.captionSize,
                  color: blockColor,
                  textAlign: "center",
                  maxWidth: 220,
                  fontWeight: isDanger ? 700 : 400,
                }}
              >
                {block.label}
              </div>

              {/* Arrow */}
              {!isLast && (
                <div
                  style={{
                    opacity: arrowOpacity,
                    padding: "0 12px",
                    fontFamily: theme.fontBody,
                    fontSize: 32,
                    color: theme.textDim,
                  }}
                >
                  →
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* DefCard */}
      {defCard && (() => {
        const defOpacity = interpolate(
          frame,
          [fps * (0.4 + blocks.length * 0.35 + 0.3), fps * (0.4 + blocks.length * 0.35 + 0.7)],
          [0, 1],
          { extrapolateRight: "clamp" }
        );
        return (
          <div
            style={{
              opacity: defOpacity,
              marginTop: 48,
              fontFamily: theme.fontBody,
              fontSize: theme.captionSize,
              color: theme.textSecondary,
              textAlign: "center",
              fontStyle: "italic",
              maxWidth: 900,
            }}
          >
            {defCard}
          </div>
        );
      })()}

      {/* Source caption */}
      {sourceCaption && (() => {
        const srcOpacity = interpolate(frame, [fps * 2.0, fps * 2.3], [0, 1], { extrapolateRight: "clamp" });
        return (
          <div
            style={{
              opacity: srcOpacity,
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
        );
      })()}
    </div>
  );
};
