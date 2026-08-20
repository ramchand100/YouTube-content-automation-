import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { theme } from "../theme";

interface DataPoint {
  year: string;
  value: number; // raw number for scaling
}

interface LineChartProps {
  title: string;
  points: DataPoint[];
  yLabel?: string;       // e.g. "bcfd"
  color?: string;        // line color, defaults to theme.red
  defCard?: string;
  sourceCaption?: string;
}

export const LineChart: React.FC<LineChartProps> = ({
  title,
  points,
  yLabel,
  color,
  defCard,
  sourceCaption,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const lineColor = color ?? theme.red;
  const W = 1100;
  const H = 380;
  const padL = 80;
  const padR = 40;
  const padT = 40;
  const padB = 60;
  const innerW = W - padL - padR;
  const innerH = H - padT - padB;

  const maxVal = Math.max(...points.map((p) => p.value));
  const minVal = Math.min(...points.map((p) => p.value));
  const range = maxVal - minVal || 1;

  const toX = (i: number) => padL + (i / (points.length - 1)) * innerW;
  const toY = (v: number) => padT + innerH - ((v - minVal) / range) * innerH;

  const totalLength = points.reduce((acc, p, i) => {
    if (i === 0) return 0;
    const dx = toX(i) - toX(i - 1);
    const dy = toY(p.value) - toY(points[i - 1].value);
    return acc + Math.sqrt(dx * dx + dy * dy);
  }, 0);

  const drawProgress = interpolate(frame, [fps * 0.3, fps * 1.5], [0, 1], {
    extrapolateRight: "clamp",
  });

  const titleOpacity = interpolate(frame, [0, fps * 0.3], [0, 1], {
    extrapolateRight: "clamp",
  });

  const labelsOpacity = interpolate(frame, [fps * 1.3, fps * 1.6], [0, 1], {
    extrapolateRight: "clamp",
  });

  const pathD = points
    .map((p, i) => `${i === 0 ? "M" : "L"} ${toX(i)} ${toY(p.value)}`)
    .join(" ");

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
          marginBottom: 40,
          alignSelf: "flex-start",
        }}
      >
        {title}
      </div>

      {/* SVG Chart */}
      <svg width={W} height={H} style={{ overflow: "visible" }}>
        {/* Grid lines */}
        {[0, 0.25, 0.5, 0.75, 1].map((t) => {
          const y = padT + innerH * (1 - t);
          return (
            <line
              key={t}
              x1={padL}
              y1={y}
              x2={padL + innerW}
              y2={y}
              stroke={theme.border}
              strokeWidth={1}
            />
          );
        })}

        {/* Axis */}
        <line x1={padL} y1={padT} x2={padL} y2={padT + innerH} stroke={theme.borderStrong} strokeWidth={2} />
        <line x1={padL} y1={padT + innerH} x2={padL + innerW} y2={padT + innerH} stroke={theme.borderStrong} strokeWidth={2} />

        {/* Animated line */}
        <path
          d={pathD}
          fill="none"
          stroke={lineColor}
          strokeWidth={4}
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeDasharray={totalLength}
          strokeDashoffset={(1 - drawProgress) * totalLength}
        />

        {/* Data points */}
        {points.map((p, i) => {
          const dotOpacity = interpolate(
            frame,
            [fps * (0.3 + i * 0.15), fps * (0.4 + i * 0.15)],
            [0, 1],
            { extrapolateRight: "clamp" }
          );
          return (
            <circle
              key={i}
              cx={toX(i)}
              cy={toY(p.value)}
              r={6}
              fill={lineColor}
              opacity={dotOpacity}
            />
          );
        })}

        {/* X-axis labels */}
        {points.map((p, i) => (
          <text
            key={i}
            x={toX(i)}
            y={padT + innerH + 28}
            textAnchor="middle"
            fontSize={16}
            fill={theme.textSecondary}
            fontFamily="Inter, sans-serif"
            opacity={labelsOpacity}
          >
            {p.year}
          </text>
        ))}

        {/* Y-label */}
        {yLabel && (
          <text
            x={padL - 12}
            y={padT - 10}
            textAnchor="end"
            fontSize={16}
            fill={theme.textSecondary}
            fontFamily="Inter, sans-serif"
            opacity={labelsOpacity}
          >
            {yLabel}
          </text>
        )}
      </svg>

      {/* DefCard */}
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
