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
