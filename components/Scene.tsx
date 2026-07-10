"use client";

import { Canvas, useFrame, type ThreeElements } from "@react-three/fiber";
import { Float, RoundedBox, Environment, Lightformer } from "@react-three/drei";
import { useRef, useMemo } from "react";
import * as THREE from "three";

/* --- חומר זהב מטאלי --- */
function useGoldMaterial(bright = 0) {
  return useMemo(
    () =>
      new THREE.MeshStandardMaterial({
        color: new THREE.Color("#d4af37").lerp(new THREE.Color("#f7ead0"), bright),
        metalness: 1,
        roughness: 0.22,
        emissive: new THREE.Color("#3a2c07"),
        emissiveIntensity: 0.25,
      }),
    [bright]
  );
}

/* --- אות X תלת ממדית (שני מוטות מוצלבים) --- */
function XMark({ scale = 1, ...props }: { scale?: number } & ThreeElements["group"]) {
  const mat = useGoldMaterial(0.1);
  return (
    <group scale={scale} {...props}>
      <RoundedBox args={[0.42, 2.1, 0.42]} radius={0.12} smoothness={4} rotation={[0, 0, Math.PI / 4]} material={mat} />
      <RoundedBox args={[0.42, 2.1, 0.42]} radius={0.12} smoothness={4} rotation={[0, 0, -Math.PI / 4]} material={mat} />
    </group>
  );
}

/* --- טבעת O תלת ממדית --- */
function ORing({ scale = 1, white = false, ...props }: { scale?: number; white?: boolean } & ThreeElements["group"]) {
  const gold = useGoldMaterial(0);
  const whiteMat = useMemo(
    () => new THREE.MeshStandardMaterial({ color: "#f4f2ee", metalness: 0.6, roughness: 0.3 }),
    []
  );
  return (
    <group scale={scale} {...props}>
      <mesh material={white ? whiteMat : gold}>
        <torusGeometry args={[0.95, 0.24, 24, 64]} />
      </mesh>
    </group>
  );
}

/* --- ריחוף עדין + היענות לעכבר --- */
function Cluster() {
  const group = useRef<THREE.Group>(null);
  useFrame((state) => {
    if (!group.current) return;
    const t = state.clock.elapsedTime;
    group.current.rotation.y = Math.sin(t * 0.12) * 0.28 + state.pointer.x * 0.35;
    group.current.rotation.x = Math.cos(t * 0.1) * 0.12 - state.pointer.y * 0.2;
  });

  return (
    <group ref={group}>
      <Float speed={1.4} rotationIntensity={0.6} floatIntensity={0.9}>
        <XMark scale={1.35} position={[0, 0.1, 0]} rotation={[0.2, 0.4, 0]} />
      </Float>
      <Float speed={1.1} rotationIntensity={0.5} floatIntensity={1.1}>
        <ORing scale={1} position={[2.7, 1.1, -1.2]} rotation={[0.6, 0.2, 0]} />
      </Float>
      <Float speed={1.7} rotationIntensity={0.7} floatIntensity={1.2}>
        <XMark scale={0.7} position={[-2.9, 1.4, -1.4]} rotation={[0.3, -0.4, 0.6]} />
      </Float>
      <Float speed={1.3} rotationIntensity={0.5} floatIntensity={1}>
        <ORing scale={0.6} white position={[-2.3, -1.7, -0.8]} rotation={[0.4, 0.3, 0]} />
      </Float>
      <Float speed={1.5} rotationIntensity={0.6} floatIntensity={1.3}>
        <XMark scale={0.5} position={[2.5, -1.8, -0.6]} rotation={[0.1, 0.5, -0.4]} />
      </Float>
      <Float speed={1} rotationIntensity={0.4} floatIntensity={0.8}>
        <ORing scale={0.42} position={[3.7, -0.6, -2]} rotation={[0.5, 0, 0]} />
      </Float>
    </group>
  );
}

export default function Scene() {
  return (
    <Canvas
      dpr={[1, 1.8]}
      camera={{ position: [0, 0, 8], fov: 42 }}
      gl={{ antialias: true, alpha: true, powerPreference: "high-performance" }}
      style={{ pointerEvents: "none" }}
    >
      <ambientLight intensity={0.35} />
      <spotLight position={[6, 8, 6]} angle={0.4} penumbra={1} intensity={2.4} color="#fff3d6" />
      <pointLight position={[-6, -4, 2]} intensity={1.4} color="#d4af37" />
      <Cluster />
      {/* סביבת תאורה ליצירת השתקפויות זהב — ללא קבצים חיצוניים */}
      <Environment resolution={128}>
        <Lightformer form="rect" intensity={3} position={[0, 4, -6]} scale={[10, 6, 1]} color="#fff6df" />
        <Lightformer form="rect" intensity={2} position={[-5, -2, -4]} scale={[6, 6, 1]} color="#d4af37" />
        <Lightformer form="circle" intensity={2.5} position={[5, 2, 2]} scale={4} color="#ffffff" />
      </Environment>
    </Canvas>
  );
}
