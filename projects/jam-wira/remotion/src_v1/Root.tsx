import React from 'react';
import {Composition} from 'remotion';
import {Main} from './Main';
import data from './data.json';
export const Root: React.FC = () => (
  <Composition id="JamWira" component={Main} durationInFrames={Math.round((data.dur + data.tail) * 30)}
    fps={30} width={1080} height={1920} defaultProps={{showSafe: false}} />
);
