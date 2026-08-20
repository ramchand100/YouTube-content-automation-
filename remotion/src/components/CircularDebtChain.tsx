import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { theme } from "../theme";

interface DebtNode {
  actor: string;          // e.g. "SNGPL / SSGCL"
  owes: string;           // what they owe, e.g. "Rs. 400B"
  owesTo: string;         // to whom
  color?: string;         // accent; defaults to theme.red
}

interface CircularDebtChainProps {
  title?: string;
  nodes: DebtNode[];
  totalLabel?: string;    // e.g. "Total Gas Circular Debt: Rs. 2+ Trillion"
  sourceCaption?: string;
}

export const CircularDebtChain: React.FC<CircularDebtChainProps> = ({
  title,
  nodes,
  totalLabel,
  sourceCaption,
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
            marginBottom: 48,
          }}
        >
          {title}
        </div>
      )}

      {/* Chain of debt nodes */}
      <div style={{ display: "flex", flexDirection: "column", gap: 0, width: "100%", maxWidth: 1100 }}>
        {nodes.map((node, i) => {
          const delay = fps * (0.3 + i * 0.4);
          const nodeOpacity = interpolate(frame, [delay, delay + fps * 0.3], [0, 1], { extrapolateRight: "clamp" });
          const nodeSlide = interpolate(frame, [delay, delay + fps * 0.3], [30, 0], { extrapolateRight: "clamp" });
          const accentColor = node.color ?? theme.red;
          const isLast = i === nodes.length - 1;

          return (
            <div key={i} style={{ display: "flex", flexDirection: "column", alignItems: "flex-start" }}>
              {/* Node row */}
              <div
                style={{
                  opacity: nodeOpacity,
                  transform: `translateX(${nodeSlide}px)`,
                  backgroundColor: theme.cardBg,
                  boxShadow: theme.cardShadow,
                  borderLeft: `6px solid ${accentColor}`,
                  borderRadius: 10,
                  padding: "20px 32px",
                  display: "flex",
                  alignItems: "center",
                  gap: 40,
                  width: "100%",
                }}
              >
                {/* Actor */}
                <div style={{ flex: "0 0 300px", fontFamily: theme.fontBody, fontSize: theme.bodySize, color: theme.text, fontWeight: 600 }}>
                  {node.actor}
                </div>
                {/* Arrow + amount */}
                <div style={{ display: "flex", alignItems: "center", gap: 16, flex: 1 }}>
                  <div style={{ fontFamily: theme.fontTitle, fontSize: theme.subheadingSize, color: accentColor }}>
                    {node.owes}
                  </div>
                  <div style={{ fontSize: 24, color: theme.textDim }}>→</div>
                  <div style={{ fontFamily: theme.fontBody, fontSize: theme.bodySize, color: theme.textSecondary }}>
                    {node.owesTo}
                  </div>
                </div>
              </div>

              {/* Connector line to next */}
              {!isLast && (
                <div
                  style={{
                    opacity: nodeOpacity,
                    marginLeft: 32,
                    width: 2,
                    height: 24,
                    backgroundColor: theme.border,
                  }}
                />
              )}
            </div>
          );
        })}
      </div>

      {/* Total label */}
      {totalLabel && (() => {
        const totalDelay = fps * (0.3 + nodes.length * 0.4 + 0.3);
        const totalOpacity = interpolate(frame, [totalDelay, totalDelay + fps * 0.4], [0, 1], { extrapolateRight: "clamp" });
        return (
          <div
            style={{
              opacity: totalOpacity,
              marginTop: 40,
              backgroundColor: theme.redLight,
              border: `2px solid ${theme.red}`,
              borderRadius: 10,
              padding: "18px 48px",
              fontFamily: theme.fontTitle,
              fontSize: theme.subheadingSize,
              color: theme.red,
            }}
          >
            {totalLabel}
          </div>
        );
      })()}

      {/* Source caption */}
      {sourceCaption && (() => {
        const srcOpacity = interpolate(frame, [fps * 2.5, fps * 2.8], [0, 1], { extrapolateRight: "clamp" });
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
