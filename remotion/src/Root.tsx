import React from 'react';
import {Composition} from 'remotion';
import {FeeSplit} from './scenes/FeeSplit';
import feeSplitData from './data/feeSplit.json';

// Register every scene as a Composition. Props come from JSON in src/data, so the
// same component renders any episode's numbers. Preview with `npm run studio`.
export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="FeeSplit"
        component={FeeSplit}
        durationInFrames={300}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={feeSplitData}
      />
    </>
  );
};
