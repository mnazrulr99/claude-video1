import React from 'react';
import {
  AbsoluteFill, Audio, OffthreadVideo, Sequence, interpolate, spring,
  staticFile, useCurrentFrame, useVideoConfig, Easing, delayRender, continueRender,
} from 'remotion';
import data from './data.json';
import {MONT_B64, FRED_B64, CAV_B64} from './fontdata';

const MONT = 'MontLocal';
const FRED = 'FredLocal';
const CAV = 'CavLocal';
const b64 = (s: string) => Uint8Array.from(atob(s), (c) => c.charCodeAt(0)).buffer;
if (typeof document !== 'undefined' && !(window as any).__lf) {
  (window as any).__lf = true;
  const a = new FontFace('MontLocal', b64(MONT_B64), {weight: '900'});
  const b = new FontFace('FredLocal', b64(FRED_B64), {weight: '700'});
  const c = new FontFace('CavLocal', b64(CAV_B64), {weight: '700'});
  document.fonts.add(a); document.fonts.add(b); document.fonts.add(c);
}

const FPS = 30;
const MINT = '#7CF29C';
const INK = '#111111';
const f = (t: number) => Math.round(t * FPS);
// Safe band: top titles centred at y=300 (TikTok/IG top UI ends ~250), captions at y=1300 (bottom UI starts ~1440).
const TITLE_Y = 250;
const CAPTION_Y = 1340;
const EMOJI = '"Noto Color Emoji"';

type Ev = any;

const usePop = (startF: number, endF: number, damping = 11) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const inn = spring({frame: frame - startF, fps, config: {damping, stiffness: 180, mass: 0.7}});
  const out = interpolate(frame, [endF - 5, endF], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return {scale: inn * (0.6 + 0.4 * out), opacity: Math.min(1, inn * 1.5) * out, inn};
};

/* ---------------- VIDEO with zoom pattern ---------------- */
const VideoLayer: React.FC = () => {
  const frame = useCurrentFrame();
  const t = frame / FPS;
  let base = 1;
  data.segs.forEach((s, i) => {
    if (t >= s.s && t < s.e) base = i % 2 === 1 ? 1.1 : 1.0;
  });
  // hook crash-zoom
  const crash = interpolate(frame, [0, 8], [1.28, 1], {extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic)});
  // emphasis punches
  let punch = 1;
  let oy = 0.34;
  (data.ev as Ev[]).filter((e) => e.type === 'punch').forEach((e) => {
    const a = f(e.s), b = f(e.e);
    if (frame >= a && frame <= b + 6) {
      const k = interpolate(frame, [a, a + 3, b, b + 6], [0, 1, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
      punch = 1 + (e.z - 1) * k;
      if (e.oy) oy = e.oy;
    }
  });
  const scale = (frame < 8 ? crash : base) * punch;
  let flash = interpolate(frame, [0, 4], [0.85, 0], {extrapolateRight: 'clamp'});
  (data.ev as Ev[]).filter((e) => e.type === 'flash').forEach((e) => {
    const a = f(e.s);
    if (frame >= a - 2 && frame <= a + 6) flash = Math.max(flash, interpolate(frame, [a - 2, a, a + 6], [0, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  });
  const br = (data.ev as Ev[]).find((e) => e.type === 'broll' && frame >= f(e.s) && frame < f(e.e));
  return (
    <AbsoluteFill style={{backgroundColor: 'black'}}>
      <AbsoluteFill style={{transform: `scale(${scale})`, transformOrigin: `50% ${oy * 100}%`}}>
        <OffthreadVideo src={staticFile('cut_video.mp4')} muted style={{width: '100%', height: '100%'}} />
      </AbsoluteFill>
      {(data.ev as Ev[]).filter((e) => e.type === 'broll').map((e) => (
        <Sequence key={'br' + e.s} from={f(e.s)} durationInFrames={f(e.e) - f(e.s)} layout="none">
          <AbsoluteFill style={{transform: `scale(${interpolate(frame - f(e.s), [0, f(e.e) - f(e.s)], [1.12, 1.0])})`, opacity: br ? 1 : 0}}>
            <OffthreadVideo src={staticFile('raw.mp4')} startFrom={f(e.src)} muted style={{width: '100%', height: '100%'}} />
          </AbsoluteFill>
        </Sequence>
      ))}
      <AbsoluteFill style={{backgroundColor: 'white', opacity: flash}} />
    </AbsoluteFill>
  );
};

/* ---------------- CAPTIONS (karaoke) ---------------- */
const Captions: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = frame / FPS;
  const cap = data.caps.find((c) => t >= c.s && t < c.e + 0.05);
  if (!cap) return null;
  const pop = spring({frame: frame - f(cap.s), fps, config: {damping: 12, stiffness: 220, mass: 0.6}});
  return (
    <div style={{position: 'absolute', top: CAPTION_Y, left: 90, right: 150, display: 'flex', justifyContent: 'center',
      flexWrap: 'wrap', gap: '0 28px', transform: `translateY(-50%) scale(${0.85 + 0.15 * pop})`}}>
      {cap.w.map((w, i) => {
        const active = t >= w.s - 0.03 && t < (cap.w[i + 1]?.s ?? cap.e + 0.05);
        return (
          <span key={i} style={{
            fontFamily: MONT, fontWeight: 900, fontSize: 82, lineHeight: 1.1, letterSpacing: 1,
            color: active ? MINT : 'white', WebkitTextStroke: '12px black', paintOrder: 'stroke fill',
            textShadow: '0 6px 14px rgba(0,0,0,0.55)', display: 'inline-block',
            transform: `scale(${active ? 1.08 : 1})`,
          }}>{w.t}</span>
        );
      })}
    </div>
  );
};

/* ---------------- GRAPHICS ---------------- */
const TopCard: React.FC<{s: number; e: number; children: React.ReactNode; bg?: string; rot?: number}> = ({s, e, children, bg = 'white', rot = -2}) => {
  const {scale, opacity} = usePop(f(s), f(e));
  return (
    <div style={{position: 'absolute', top: TITLE_Y, left: 0, right: 0, display: 'flex', justifyContent: 'center', opacity}}>
      <div style={{background: bg, borderRadius: 30, padding: '16px 34px', transform: `scale(${scale}) rotate(${rot}deg)`,
        boxShadow: '0 10px 0 rgba(0,0,0,0.85), 0 18px 30px rgba(0,0,0,0.35)', border: '5px solid #111',
        fontFamily: FRED, fontWeight: 700, fontSize: 62, color: INK, display: 'flex', alignItems: 'center', gap: 16, whiteSpace: 'nowrap'}}>
        {children}
      </div>
    </div>
  );
};
const Emo: React.FC<{c: string; size?: number}> = ({c, size = 62}) => <span style={{fontFamily: EMOJI, fontSize: size}}>{c}</span>;

const HookTitle: React.FC<{e: Ev}> = ({e}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const ok = frame >= f(e.ok);
  const stamp = spring({frame: frame - f(e.x), fps, config: {damping: 9, stiffness: 260}});
  const swap = spring({frame: frame - f(e.ok), fps, config: {damping: 10, stiffness: 200}});
  return (
    <TopCard s={e.s} e={e.e} bg={ok ? MINT : 'white'} rot={ok ? 2 : -2}>
      {!ok ? (
        <div style={{position: 'relative'}}>
          <span>SMARTWATCH?</span>
          {frame >= f(e.x) && (
            <span style={{position: 'absolute', left: '50%', top: '50%', fontFamily: EMOJI, fontSize: 120,
              transform: `translate(-50%,-50%) scale(${3 - 2 * stamp}) rotate(${-15 * (1 - stamp)}deg)`, opacity: Math.min(1, stamp * 2)}}>❌</span>
          )}
        </div>
      ) : (
        <span style={{transform: `scale(${0.7 + 0.3 * swap})`, display: 'flex', alignItems: 'center', gap: 14}}>
          JAM BUDAK SEKOLAH <Emo c="✅" />
        </span>
      )}
    </TopCard>
  );
};

const Shine: React.FC<{e: Ev}> = ({e}) => {
  const frame = useCurrentFrame();
  const x = interpolate(frame, [f(e.s), f(e.e)], [-700, 1500], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <div style={{position: 'absolute', top: -400, left: x, width: 260, height: 2800, transform: 'rotate(20deg)',
      background: 'linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.45), rgba(255,255,255,0))'}} />
  );
};

const Pill: React.FC<{e: Ev}> = ({e}) => (
  <TopCard s={e.s} e={e.e} bg="#111" rot={0}>
    <Emo c={e.emoji} /><span style={{color: MINT}}>{e.text}</span>
  </TopCard>
);

const Title: React.FC<{e: Ev}> = ({e}) => (
  <TopCard s={e.s} e={e.e}><span>{e.text}</span><Emo c={e.emoji} /></TopCard>
);

const Swatches: React.FC<{e: Ev}> = ({e}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const out = interpolate(frame, [f(e.e) - 5, f(e.e)], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const picked = frame >= f(e.pick);
  const items = [
    {c: '#FFB3D1', l: 'PINK', t: e.pink},
    {c: '#FFFFFF', l: 'PUTIH', t: e.white},
    {c: '#9FE6B8', l: 'HIJAU', t: e.green},
  ];
  const pk = spring({frame: frame - f(e.pick), fps, config: {damping: 10}});
  return (
    <div style={{position: 'absolute', top: TITLE_Y - 10, left: 0, right: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', opacity: out}}>
      <div style={{display: 'flex', gap: 46}}>
        {items.map((it, i) => {
          const s = spring({frame: frame - f(it.t), fps, config: {damping: 9, stiffness: 220}});
          const isG = i === 2;
          return (
            <div key={i} style={{display: 'flex', flexDirection: 'column', alignItems: 'center', transform: `scale(${s * (picked && isG ? 1 + 0.18 * pk : 1)})`,
              opacity: picked && !isG ? 0.45 : 1}}>
              <div style={{width: 100, height: 100, borderRadius: 60, background: it.c, border: `${picked && isG ? 10 : 6}px solid ${picked && isG ? MINT : '#111'}`,
                boxShadow: '0 8px 0 rgba(0,0,0,0.8)', display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                {picked && isG && <Emo c="✅" size={56} />}
              </div>
              <div style={{marginTop: 8, fontFamily: FRED, fontWeight: 700, fontSize: 58, color: isG ? '#7CF29C' : it.c, WebkitTextStroke: '10px #111', paintOrder: 'stroke fill', textShadow: '0 6px 0 rgba(0,0,0,0.6)'}}>{it.l}</div>
            </div>
          );
        })}
      </div>
      {picked && (
        <div style={{marginTop: 14, background: MINT, border: '5px solid #111', borderRadius: 24, padding: '8px 26px', fontFamily: FRED, fontWeight: 700,
          fontSize: 46, transform: `scale(${pk}) rotate(-2deg)`, boxShadow: '0 7px 0 rgba(0,0,0,0.85)'}}>
          PILIHAN WIRA <Emo c="💚" size={44} />
        </div>
      )}
    </div>
  );
};

const SideBadge: React.FC<{s: number; e: number; color: string; children: React.ReactNode}> = ({s, e, color, children}) => {
  const frame = useCurrentFrame();
  const {scale, opacity} = usePop(f(s), f(e), 9);
  const bob = Math.sin(frame / 7) * 6;
  return (
    <div style={{position: 'absolute', left: 54, top: 470 + bob, opacity, transform: `scale(${scale}) rotate(-5deg)`, transformOrigin: 'left center'}}>
      <div style={{background: 'white', border: `7px solid ${color}`, outline: '5px solid #111', borderRadius: 34, padding: '16px 22px', width: 270,
        display: 'flex', flexDirection: 'column', alignItems: 'center', boxShadow: '0 10px 0 rgba(0,0,0,0.8)'}}>
        {children}
      </div>
    </div>
  );
};

const Badge: React.FC<{e: Ev}> = ({e}) => (
  <SideBadge s={e.s} e={e.e} color={e.color}>
    <Emo c={e.emoji} size={90} />
    <div style={{fontFamily: MONT, fontWeight: 900, fontSize: 38, textAlign: 'center', lineHeight: 1.1, whiteSpace: 'pre-line', color: INK}}>{e.text}</div>
    {e.foot && <div style={{marginTop: 10, background: '#FFD23F', border: '4px solid #111', borderRadius: 14, padding: '4px 10px', fontFamily: MONT, fontWeight: 900, fontSize: 22, color: INK, whiteSpace: 'nowrap'}}>
      <span style={{fontFamily: EMOJI}}>{e.foot.slice(0, 2)}</span>{e.foot.slice(2)}</div>}
  </SideBadge>
);

const Sticker: React.FC<{e: Ev}> = ({e}) => {
  const frame = useCurrentFrame();
  const {scale, opacity} = usePop(f(e.s), f(e.e), 7);
  const wig = Math.sin(frame / 3) * 3;
  return (
    <div style={{position: 'absolute', top: TITLE_Y - 20, left: 0, right: 0, display: 'flex', justifyContent: 'center', opacity}}>
      <div style={{transform: `scale(${scale}) rotate(${wig}deg)`, background: 'linear-gradient(180deg,#FFE45C,#FFB400)', border: '6px solid #111',
        borderRadius: 999, padding: '18px 44px', fontFamily: FRED, fontWeight: 700, fontSize: 74, color: INK, boxShadow: '0 10px 0 rgba(0,0,0,0.85)',
        display: 'flex', gap: 14, alignItems: 'center'}}>
        <Emo c={e.emoji} size={70} />{e.text}<Emo c={e.emoji} size={70} />
      </div>
    </div>
  );
};

const Chips: React.FC<{e: Ev}> = ({e}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const out = interpolate(frame, [f(e.e) - 5, f(e.e)], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const chip = (t: number, label: string, bg: string, rot: number) => {
    const s = spring({frame: frame - f(t), fps, config: {damping: 8, stiffness: 240}});
    return (
      <div style={{transform: `scale(${s}) rotate(${rot}deg)`, background: bg, border: '6px solid #111', borderRadius: 26, padding: '12px 40px',
        fontFamily: FRED, fontWeight: 700, fontSize: 84, color: INK, boxShadow: '0 9px 0 rgba(0,0,0,0.85)'}}>{label}</div>
    );
  };
  return (
    <div style={{position: 'absolute', top: TITLE_Y - 10, left: 0, right: 0, display: 'flex', justifyContent: 'center', gap: 40, opacity: out}}>
      {chip(e.a, 'ABC', '#FFB3D1', -5)}
      {chip(e.b, '123', '#8FD3FF', 4)}
    </div>
  );
};

const Clock: React.FC<{e: Ev}> = ({e}) => {
  const frame = useCurrentFrame();
  const {scale, opacity} = usePop(f(e.s), f(e.e), 10);
  const hourA = frame >= f(e.a) && frame < f(e.b);
  const minA = frame >= f(e.b);
  const minRot = (frame - f(e.s)) * 6; // sweeping
  const hrRot = 120 + (frame - f(e.s)) * 0.5;
  const R = 120;
  const hl = (on: boolean) => (on ? '#FF6B3D' : '#111');
  return (
    <div style={{position: 'absolute', left: 50, top: 450, opacity, transform: `scale(${scale})`, transformOrigin: 'left center',
      display: 'flex', flexDirection: 'column', alignItems: 'center', width: 300}}>
      <svg width={2 * R + 30} height={2 * R + 30} viewBox={`${-R - 15} ${-R - 15} ${2 * R + 30} ${2 * R + 30}`}>
        <circle r={R + 6} fill="#111" />
        <circle r={R - 4} fill="#CFF8DA" stroke={MINT} strokeWidth={10} />
        {[12, 3, 6, 9].map((n, i) => {
          const a = (i * 90 - 90) * (Math.PI / 180);
          return <text key={n} x={Math.cos(a) * (R - 34)} y={Math.sin(a) * (R - 34) + 14} textAnchor="middle" fontFamily={MONT} fontWeight={900} fontSize={38} fill="#111">{n}</text>;
        })}
        {Array.from({length: 12}).map((_, i) => {
          const a = (i * 30) * (Math.PI / 180);
          return i % 3 ? <circle key={i} cx={Math.cos(a) * (R - 26)} cy={Math.sin(a) * (R - 26)} r={5} fill="#111" /> : null;
        })}
        <line x1={0} y1={0} x2={0} y2={-R * 0.45} stroke={hl(hourA)} strokeWidth={hourA ? 20 : 14} strokeLinecap="round" transform={`rotate(${hrRot})`} />
        <line x1={0} y1={0} x2={0} y2={-R * 0.75} stroke={hl(minA)} strokeWidth={minA ? 14 : 9} strokeLinecap="round" transform={`rotate(${minRot})`} />
        <circle r={12} fill="#111" />
      </svg>
      <div style={{marginTop: 6, background: hourA || minA ? '#FF6B3D' : 'white', border: '5px solid #111', borderRadius: 20, padding: '6px 18px',
        fontFamily: MONT, fontWeight: 900, fontSize: 34, color: hourA || minA ? 'white' : INK, boxShadow: '0 6px 0 rgba(0,0,0,0.85)'}}>
        {minA ? 'JARUM PANJANG' : 'JARUM KECIL'}
      </div>
    </div>
  );
};

const Cta: React.FC<{e: Ev}> = ({e}) => {
  const frame = useCurrentFrame();
  const {scale, opacity} = usePop(f(e.s), f(e.e) + 30);
  const bounce = Math.abs(Math.sin(frame / 5)) * -14;
  return (
    <div style={{position: 'absolute', top: TITLE_Y - 10, left: 0, right: 0, display: 'flex', justifyContent: 'center', opacity}}>
      <div style={{transform: `scale(${scale * interpolate(frame - f(e.s), [0, 5], [1.9, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})}) rotate(${interpolate(frame - f(e.s), [0, 5], [-12, -3], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})}deg)`, background: '#FFD23F', border: '6px solid #111', borderRadius: 32, padding: '16px 30px',
        boxShadow: '0 10px 0 rgba(0,0,0,0.85)', display: 'flex', alignItems: 'center', gap: 18}}>
        <span style={{fontFamily: EMOJI, fontSize: 84, transform: `translateY(${bounce}px)`, display: 'inline-block'}}>🛒</span>
        <div style={{fontFamily: FRED, fontWeight: 700, color: INK, lineHeight: 1.0}}>
          <div style={{fontSize: 40}}>TEKAN</div>
          <div style={{fontSize: 62}}>BEG KUNING</div>
        </div>
        <span style={{fontFamily: EMOJI, fontSize: 64, transform: `translateY(${-bounce}px)`, display: 'inline-block'}}>👇</span>
      </div>
    </div>
  );
};

const PinkNote: React.FC<{e: Ev}> = ({e}) => (
  <SideBadge s={e.s} e={e.e} color="#FF7EB6">
    <div style={{width: 90, height: 90, borderRadius: 50, background: '#FFB3D1', border: '6px solid #111'}} />
    <div style={{fontFamily: MONT, fontWeight: 900, fontSize: 36, textAlign: 'center', lineHeight: 1.1, color: INK, marginTop: 8}}>ADA WARNA<br />PINK <Emo c="💗" size={36} /></div>
  </SideBadge>
);

const Note: React.FC<{e: Ev}> = ({e}) => {
  const frame = useCurrentFrame();
  const a = f(e.s);
  const write = interpolate(frame, [a, a + 14], [0, 100], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const arrow = interpolate(frame, [a + 8, a + 18], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const out = interpolate(frame, [f(e.e) - 5, f(e.e)], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <div style={{position: 'absolute', left: 300, top: 250, opacity: out}}>
      <div style={{fontFamily: CAV, fontWeight: 700, fontSize: 84, color: 'white', transform: 'rotate(-6deg)', clipPath: `inset(0 ${100 - write}% 0 0)`,
        textShadow: '0 4px 0 #111, 0 0 14px rgba(0,0,0,0.6)', whiteSpace: 'nowrap'}}>{e.text}</div>
      <svg width={360} height={300} style={{position: 'absolute', left: 420, top: 95, overflow: 'visible'}}>
        <path d="M 10 10 C 110 20, 150 150, 112 290" fill="none" stroke="white" strokeWidth={9} strokeLinecap="round" pathLength={1}
          strokeDasharray={1} strokeDashoffset={arrow} style={{filter: 'drop-shadow(0 3px 0 #111)'}} />
        <path d="M 84 264 L 111 292 L 134 260" fill="none" stroke="white" strokeWidth={9} strokeLinecap="round" strokeLinejoin="round"
          opacity={arrow < 0.05 ? 1 : 0} style={{filter: 'drop-shadow(0 3px 0 #111)'}} />
      </svg>
    </div>
  );
};

const Graphic: React.FC<{e: Ev}> = ({e}) => {
  switch (e.type) {
    case 'hookTitle': return <HookTitle e={e} />;
    case 'shine': return <Shine e={e} />;
    case 'pill': return <Pill e={e} />;
    case 'title': return <Title e={e} />;
    case 'swatches': return <Swatches e={e} />;
    case 'badge': return <Badge e={e} />;
    case 'sticker': return <Sticker e={e} />;
    case 'chips': return <Chips e={e} />;
    case 'clock': return <Clock e={e} />;
    case 'cta': return <Cta e={e} />;
    case 'pinkNote': return <PinkNote e={e} />;
    case 'note': return <Note e={e} />;
    default: return null;
  }
};

const SafeGuides: React.FC = () => (
  <AbsoluteFill style={{pointerEvents: 'none'}}>
    <div style={{position: 'absolute', top: 0, left: 0, right: 0, height: 220, background: 'rgba(255,0,0,0.28)'}} />
    <div style={{position: 'absolute', bottom: 0, left: 0, right: 0, height: 480, background: 'rgba(255,0,0,0.28)'}} />
    <div style={{position: 'absolute', top: 220, bottom: 480, right: 0, width: 140, background: 'rgba(255,0,0,0.28)'}} />
    <div style={{position: 'absolute', top: 1450, left: 20, color: 'white', fontFamily: MONT, fontWeight: 900, fontSize: 30}}>TIKTOK/IG UI ZONE</div>
  </AbsoluteFill>
);

export const Main: React.FC<{showSafe: boolean}> = ({showSafe}) => {
  const frame = useCurrentFrame();
  const endF = f(data.dur);
  const black = interpolate(frame, [endF - 2, endF + 2], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const totalF = f(data.dur + data.tail);
  return (
    <AbsoluteFill style={{backgroundColor: 'black'}}>
      <VideoLayer />
      {(data.ev as Ev[]).filter((e) => e.type !== 'punch' && e.type !== 'broll' && e.type !== 'flash' && frame >= f(e.s) - 1 && frame <= f(e.e) + 35).map((e, i) => (
        <Graphic key={e.type + e.s} e={e} />
      ))}
      <Captions />
      <AbsoluteFill style={{backgroundColor: 'black', opacity: black}} />
      {showSafe && <SafeGuides />}
      {/* AUDIO */}
      <Audio src={staticFile('voice.wav')} />
      {data.sfx.map((s, i) => (
        <Sequence key={'s' + i} from={f(s.t)} layout="none">
          <Audio src={staticFile(`sfx/${s.n}.mp3`)} volume={s.v} />
        </Sequence>
      ))}
      <Sequence from={endF} layout="none"><Audio src={staticFile('sfx/ding.mp3')} volume={0.5} /></Sequence>
    </AbsoluteFill>
  );
};
