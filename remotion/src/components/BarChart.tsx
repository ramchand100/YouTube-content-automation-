import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { theme } from "../theme";

interface Bar {
  label: string;
  value: number;       // raw number for scaling
  displayValue: string; // e.g. "~3.5 bcfd"
  color?: string;
  sourceCaption?: string;
}

interface GapLabel {
  label: string;
  color?: string;
}

interface BarChartProps {
  title: string;
  bars: Bar[];
  gap?: GapLabel;           // optional gap annotation between bars 0 and 1
  defCard?: string;         // optional definition shown below
  sourceCaption?: string;   // global source caption
}

export const BarChart: React.FC<BarChartProps> = ({
  title,
  bars,
  gap,
  defCard,
  sourceCaption,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const maxVal = Math.max(...bars.map((b) => b.value));
  const maxBarHeight = 380;

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
        padding: "60px 120px",
        boxSizing: "border-box",
      }}
    >
      {/* Title */}
      <div
        style={{
          opacity: titleOpacity,
          fontFamily: theme.fontBody,
          fontSize: theme.captionSize,
          color: theme.textSecondary,
          textTransform: "uppercase",
          letterSpacing: 3,
          marginBottom: 48,
          alignSelf: "flex-start",
        }}
      >
        {title}
      </div>

      {/* Bars */}
      <div style={{ display: "flex", alignItems: "flex-end", gap: 32, width: "100%", justifyContent: "center" }}>
        {bars.map((bar, i) => {
          const delay = fps * (0.3 + i * 0.4);
          const barH = (bar.value / maxVal) * maxBarHeight;
          const animatedH = interpolate(frame, [delay, delay + fps * 0.6], [0, barH], {
            extrapolateRight: "clamp",
          });
          const labelOpacity = interpolate(frame, [delay + fps * 0.5, delay + fps * 0.8], [0, 1], {
            extrapolateRight: "clamp",
          });
          const barColor = bar.color ?? theme.green;

          return (
            <div key={i} style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 16 }}>
              {/* Value on top */}
              <div style={{ opacity: labelOpacity, fontFamily: theme.fontTitle, fontSize: theme.subheadingSize, color: barColor }}>
                {bar.displayValue}
              </div>
              {/* Bar */}
              <div
                style={{
                  width: 180,
                  height: animatedH,
                  backgroundColor: barColor,
                  borderRadius: "8px 8px 0 0",
                  opacity: 0.92,
                }}
              />
              {/* Label below */}
              <div style={{ opacity: labelOpacity, fontFamily: theme.fontBody, fontSize: theme.captionSize, color: theme.text, textAlign: "center", maxWidth: 220 }}>
                {bar.label}
              </div>
            </div>
          );
        })}
      </div>

      {/* Gap annotation */}
      {gap && bars.length >= 2 && (() => {
        const gapOpacity = interpolate(frame, [fps * 1.4, fps * 1.7], [0, 1], { extrapolateRight: "clamp" });
        return (
          <div
            style={{
              opacity: gapOpacity,
              marginTop: 40,
              backgroundColor: gap.color ? `${gap.color}18` : theme.redLight,
              border: `2px solid ${gap.color ?? theme.red}`,
              borderRadius: 10,
              padding: "16px 40px",
              fontFamily: theme.fontBody,
              fontSize: theme.bodySize,
              color: gap.color ?? theme.red,
            }}
          >
            {gap.label}
          </div>
        );
      })()}

      {/* DefCard below */}
      {defCard && (() => {
        const defOpacity = interpolate(frame, [fps * 1.8, fps * 2.1], [0, 1], { extrapolateRight: "clamp" });
        return (
          <div
            style={{
              opacity: defOpacity,
              marginTop: 32,
              fontFamily: theme.fontBody,
              fontSize: theme.captionSize,
              color: theme.textSecondary,
              textAlign: "center",
              fontStyle: "italic",
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
