"use client";

import type { SimulationResult } from "@/lib/api";

export function RiskBanner({ result }: { result: SimulationResult | null }) {
  if (!result) return null;
  const highRisk = result.risk.level === "high" || result.risk.level === "blocked";
  return (
    <section
      className={`rounded-lg border p-4 ${
        highRisk ? "border-red-200 bg-red-50 text-red-950" : "border-amber-200 bg-amber-50 text-amber-950"
      }`}
    >
      <div className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
        <h2 className="text-base font-semibold">Risk Level: {result.risk.level.toUpperCase()}</h2>
        <span className="rounded bg-white/70 px-2 py-1 text-xs font-semibold">
          Allowed output: {result.risk.allowed_output}
        </span>
      </div>
      <p className="mt-2 text-sm leading-6">{result.risk.reason}</p>
    </section>
  );
}
