import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { theme } from "../theme";

interface FlowNode {
  id: string;
  label: string;
  sublabel?: string;
  color?: string; // border/accent color; defaults to theme.border
}

interface FlowEdge {
  from: string;
  to: string;
  label?: string;
}

interface FlowDiagramProps {
  title?: string;
  nodes: FlowNode[];       // laid out left to right in order given
  edges: FlowEdge[];
  sourceCaption?: string;
  defCard?: string;
}

export const FlowDiagram: React.FC<FlowDiagramProps> = ({
  title,
  nodes,
  edges,
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

      {/* Nodes row */}
      <div style={{ display: "flex", alignItems: "center", gap: 0, justifyContent: "center", width: "100%", maxWidth: 1600 }}>
        {nodes.map((node, i) => {
          const delay = fps * (0.3 + i * 0.3);
          const nodeOpacity = interpolate(frame, [delay, delay + fps * 0.3], [0, 1], { extrapolateRight: "clamp" });
          const nodeScale = interpolate(frame, [delay, delay + fps * 0.3], [0.88, 1], { extrapolateRight: "clamp" });
          const accentColor = node.color ?? theme.green;

          // find matching edges FROM this node
          const edgesFrom = edges.filter((e) => e.from === node.id);
          const isLast = i === nodes.length - 1;

          return (
            <div key={node.id} style={{ display: "flex", alignItems: "center" }}>
              {/* Node card */}
              <div
                style={{
                  opacity: nodeOpacity,
                  transform: `scale(${nodeScale})`,
                  backgroundColor: theme.cardBg,
                  boxShadow: theme.cardShadow,
                  border: `2px solid ${accentColor}`,
                  borderTop: `6px solid ${accentColor}`,
                  borderRadius: 12,
                  padding: "24px 32px",
                  minWidth: 200,
                  maxWidth: 260,
                  textAlign: "center",
                }}
              >
                <div style={{ fontFamily: theme.fontBody, fontSize: theme.bodySize, color: theme.text, fontWeight: 600 }}>
                  {node.label}
                </div>
                {node.sublabel && (
                  <div style={{ fontFamily: theme.fontBody, fontSize: theme.captionSize, color: theme.textSecondary, marginTop: 8 }}>
                    {node.sublabel}
                  </div>
                )}
              </div>

              {/* Arrow to next node */}
              {!isLast && (() => {
                const arrowDelay = fps * (0.3 + i * 0.3 + 0.2);
                const arrowOpacity = interpolate(frame, [arrowDelay, arrowDelay + fps * 0.25], [0, 1], { extrapolateRight: "clamp" });
                const edgeLabel = edgesFrom[0]?.label;
                return (
                  <div style={{ display: "flex", flexDirection: "column", alignItems: "center", padding: "0 16px" }}>
                    {edgeLabel && (
                      <div style={{ opacity: arrowOpacity, fontFamily: theme.fontBody, fontSize: theme.captionSize, color: theme.textDim, marginBottom: 4 }}>
                        {edgeLabel}
                      </div>
                    )}
                    <div style={{ opacity: arrowOpacity, fontSize: 28, color: theme.textDim }}>→</div>
                  </div>
                );
              })()}
            </div>
          );
        })}
      </div>

      {/* DefCard */}
      {defCard && (() => {
        const defOpacity = interpolate(
          frame,
          [fps * (0.3 + nodes.length * 0.3 + 0.5), fps * (0.3 + nodes.length * 0.3 + 0.9)],
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
