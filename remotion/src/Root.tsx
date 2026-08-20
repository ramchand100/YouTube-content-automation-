import { Composition } from "remotion";
import { fps, width, height } from "./theme";

// Standalone component compositions (for individual graphic clips)
import { TitleCard } from "./components/TitleCard";
import { EndCard } from "./components/EndCard";
import { OpeningStats } from "./components/OpeningStats";
import { BarChart } from "./components/BarChart";
import { LineChart } from "./components/LineChart";
import { FlowDiagram } from "./components/FlowDiagram";
import { CircularDebtChain } from "./components/CircularDebtChain";
import { DominoChain } from "./components/DominoChain";
import { DefCard } from "./components/DefCard";

// Episode data
import ep07 from "../data/ep07_data.json";

// Episode 06 data
import ep06 from "../data/ep06_data.json";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* ── EP06 individual graphic clips ─────────────────────────────── */}

      <Composition
        id="ep06-title"
        component={TitleCard}
        durationInFrames={fps * 5}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep06.episode}
      />

      <Composition
        id="ep06-opening-stats"
        component={OpeningStats}
        durationInFrames={fps * 8}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{
          left: {
            label: ep06.openingStats.left.label,
            value: ep06.openingStats.left.value,
            color: "#1EB53A",
          },
          right: {
            label: ep06.openingStats.right.label,
            value: ep06.openingStats.right.value,
            color: "#D32F2F",
          },
          contrastLine: ep06.openingStats.contrastLine,
          sourceCaption: ep06.openingStats.sourceCaption,
        }}
      />

      <Composition
        id="ep06-production-gap"
        component={BarChart}
        durationInFrames={fps * 9}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep06.productionGap}
      />

      <Composition
        id="ep06-production-decline"
        component={LineChart}
        durationInFrames={fps * 9}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep06.productionDecline}
      />

      <Composition
        id="ep06-dual-pricing"
        component={FlowDiagram}
        durationInFrames={fps * 10}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep06.dualPricingFlow}
      />

      <Composition
        id="ep06-circular-debt"
        component={CircularDebtChain}
        durationInFrames={fps * 11}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep06.circularDebtChain}
      />

      <Composition
        id="ep06-domino"
        component={DominoChain}
        durationInFrames={fps * 12}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep06.dominoChain}
      />

      <Composition
        id="ep06-end-card"
        component={EndCard}
        durationInFrames={fps * 8}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep06.endCard}
      />

      {/* ── EP07 individual graphic clips ─────────────────────────────── */}

      <Composition
        id="ep07-title"
        component={TitleCard}
        durationInFrames={fps * 5}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep07.episode}
      />

      <Composition
        id="ep07-opening-stats"
        component={OpeningStats}
        durationInFrames={fps * 9}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{
          left: { label: ep07.openingStats.left.label, value: ep07.openingStats.left.value, color: ep07.openingStats.left.color },
          right: { label: ep07.openingStats.right.label, value: ep07.openingStats.right.value, color: ep07.openingStats.right.color },
          contrastLine: ep07.openingStats.contrastLine,
          sourceCaption: ep07.openingStats.sourceCaption,
        }}
      />

      <Composition
        id="ep07-soe-losses"
        component={BarChart}
        durationInFrames={fps * 10}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep07.soeLosses}
      />

      <Composition
        id="ep07-nationalization-timeline"
        component={DominoChain}
        durationInFrames={fps * 10}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep07.nationalizationTimeline}
      />

      <Composition
        id="ep07-seth-flow"
        component={FlowDiagram}
        durationInFrames={fps * 11}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep07.sethFlow}
      />

      <Composition
        id="ep07-domino-impact"
        component={DominoChain}
        durationInFrames={fps * 10}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep07.dominoImpact}
      />

      <Composition
        id="ep07-export-bar"
        component={BarChart}
        durationInFrames={fps * 10}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{
          title: "Textile Exports — Pakistan vs Bangladesh",
          bars: [
            { label: "Bangladesh", value: 47, displayValue: "$47B [VERIFY]", color: "#1EB53A" },
            { label: "Pakistan", value: 16.5, displayValue: "$16.5B [VERIFY]", color: "#D32F2F" },
          ],
          gap: { label: "Bangladesh exports ~3× more textiles [VERIFY — WTO data]", color: "#D32F2F" },
          sourceCaption: "WTO Trade Statistics [VERIFY]",
        }}
      />

      <Composition
        id="ep07-end-card"
        component={EndCard}
        durationInFrames={fps * 8}
        fps={fps}
        width={width}
        height={height}
        defaultProps={ep07.endCard}
      />

      {/* ── Reusable standalone compositions for future episodes ──────── */}

      <Composition
        id="DefCard"
        component={DefCard}
        durationInFrames={fps * 6}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{
          term: "Circular Debt",
          definition: "When a utility sells below cost, it cannot pay its suppliers. Suppliers cannot pay their suppliers. The unpaid bills stack up in a loop — hence circular.",
        }}
      />
    </>
  );
};
