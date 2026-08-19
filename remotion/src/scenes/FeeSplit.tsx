import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  Sequence,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {pkr, theme} from '../theme';

// One data-driven scene from Episode 02, Section 2 ("The Paper Trail"):
// a Rs2,000 card sale, the ~2% cut taken out, and where that cut goes.
// Everything below is driven by props, so Episode 03's version is the same
// component with different numbers and a different source caption.

export type Split = {
  label: string;
  sublabel: string;
  value: number;
};

export type FeeSplitProps = {
  amount: number;
  mdrPercent: number;
  splits: Split[];
  source: string;
};

const useCountUp = (to: number, start: number, duration: number): number => {
  const frame = useCurrentFrame();
  return interpolate(frame, [start, start + duration], [0, to], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
};

const Caption: React.FC<{source: string}> = ({source}) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [230, 260], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return (
    <div
      style={{
        position: 'absolute',
        bottom: 40,
        right: 48,
        maxWidth: 720,
        textAlign: 'right',
        color: theme.muted,
        fontFamily: theme.body,
        fontSize: 22,
        lineHeight: 1.35,
        opacity,
      }}
    >
      {source}
    </div>
  );
};

export const FeeSplit: React.FC<FeeSplitProps> = ({
  amount,
  mdrPercent,
  splits,
  source,
}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const mdr = (amount * mdrPercent) / 100;
  const kept = amount - mdr;

  // Beat 1: the sale amount counts up.
  const saleShown = useCountUp(amount, 8, 30);

  // Beat 2: the MDR is carved out (after ~frame 60).
  const mdrShown = useCountUp(mdr, 62, 24);
  const keptShown = interpolate(frame, [62, 86], [amount, kept], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{backgroundColor: theme.bg}}>
      {/* Header: the sale */}
      <Sequence from={0}>
        <div
          style={{
            position: 'absolute',
            top: 90,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: theme.body,
            color: theme.muted,
            fontSize: 28,
            letterSpacing: 2,
          }}
        >
          A CARD SALE
        </div>
        <div
          style={{
            position: 'absolute',
            top: 140,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: theme.display,
            color: theme.text,
            fontSize: 150,
          }}
        >
          {pkr(saleShown)}
        </div>
      </Sequence>

      {/* Beat 2: MDR carved out + what the shop keeps */}
      <Sequence from={60}>
        <div
          style={{
            position: 'absolute',
            top: 340,
            left: 0,
            right: 0,
            display: 'flex',
            justifyContent: 'center',
            gap: 80,
            fontFamily: theme.body,
          }}
        >
          <div style={{textAlign: 'center'}}>
            <div style={{color: theme.muted, fontSize: 26}}>Shop keeps</div>
            <div
              style={{
                color: theme.green,
                fontFamily: theme.display,
                fontSize: 76,
              }}
            >
              {pkr(keptShown)}
            </div>
          </div>
          <div style={{textAlign: 'center'}}>
            <div style={{color: theme.muted, fontSize: 26}}>
              Cut taken (~{mdrPercent}%)
            </div>
            <div
              style={{
                color: theme.red,
                fontFamily: theme.display,
                fontSize: 76,
              }}
            >
              {pkr(mdrShown)}
            </div>
          </div>
        </div>
      </Sequence>

      {/* Beat 3: where the cut goes */}
      <Sequence from={120}>
        <div
          style={{
            position: 'absolute',
            top: 560,
            left: 0,
            right: 0,
            textAlign: 'center',
            color: theme.muted,
            fontFamily: theme.body,
            fontSize: 26,
            letterSpacing: 1,
          }}
        >
          WHERE THAT {pkr(mdr)} GOES
        </div>
        <div
          style={{
            position: 'absolute',
            top: 620,
            left: 0,
            right: 0,
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'flex-end',
            gap: 48,
            height: 320,
          }}
        >
          {splits.map((s, i) => {
            const delay = 120 + i * 12;
            const grow = spring({
              frame: frame - delay,
              fps,
              config: {damping: 200},
            });
            const maxVal = Math.max(...splits.map((x) => x.value));
            const barHeight = interpolate(grow, [0, 1], [0, 260]) * (s.value / maxVal);
            const shownVal = interpolate(grow, [0, 1], [0, s.value]);
            return (
              <div
                key={s.label}
                style={{
                  width: 260,
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'flex-end',
                }}
              >
                <div
                  style={{
                    color: theme.red,
                    fontFamily: theme.display,
                    fontSize: 44,
                    marginBottom: 12,
                  }}
                >
                  {pkr(shownVal)}
                </div>
                <div
                  style={{
                    width: 150,
                    height: barHeight,
                    backgroundColor: theme.red,
                    borderRadius: 8,
                    opacity: 0.85,
                  }}
                />
                <div
                  style={{
                    marginTop: 16,
                    color: theme.text,
                    fontFamily: theme.body,
                    fontSize: 30,
                    fontWeight: 700,
                  }}
                >
                  {s.label}
                </div>
                <div
                  style={{
                    color: theme.muted,
                    fontFamily: theme.body,
                    fontSize: 22,
                    textAlign: 'center',
                  }}
                >
                  {s.sublabel}
                </div>
              </div>
            );
          })}
        </div>
      </Sequence>

      {/* Beat 4: the Raast contrast line */}
      <Sequence from={225}>
        <div
          style={{
            position: 'absolute',
            bottom: 130,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: theme.display,
            fontSize: 46,
            color: theme.green,
          }}
        >
          Over Raast, the same sale moves for ~Rs 0
        </div>
      </Sequence>

      <Caption source={source} />
    </AbsoluteFill>
  );
};
