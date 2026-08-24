"use client";

import type { SimulationResult } from "@/lib/api";
import { EvidenceDrawer } from "@/components/EvidenceDrawer";
import { RiskBanner } from "@/components/RiskBanner";

export function ResultDashboard({ result }: { result: SimulationResult | null }) {
  if (!result) {
    return (
      <section className="rounded-lg border border-slate-200 bg-white p-6 text-sm text-slate-500 shadow-surface">
        Results will appear after simulation.
      </section>
    );
  }

  return (
    <section className="space-y-4">
      <RiskBanner result={result} />
      <div className="rounded-lg border border-slate-200 bg-white p-4 shadow-surface">
        <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
          <div>
            <h2 className="text-xl font-semibold text-ink">{result.candidate_concept.name}</h2>
            <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-600">
              {result.candidate_concept.description}
            </p>
          </div>
          <span className="rounded-md bg-teal-50 px-3 py-2 text-sm font-semibold text-teal-900">
            {Math.round(result.confidence_score * 100)}% confidence
          </span>
        </div>
      </div>
      <div className="grid gap-4 xl:grid-cols-[0.9fr_1.1fr]">
        <section className="rounded-lg border border-slate-200 bg-white p-4">
          <h2 className="text-base font-semibold">Entity Mapping</h2>
          <div className="mt-4 space-y-3">
            {result.entities.map((entity) => (
              <div key={`${entity.raw}-${entity.normalized}`} className="rounded-md border border-slate-200 p-3">
                <div className="flex items-center justify-between gap-3">
                  <span className="text-sm font-semibold">{entity.raw}</span>
                  <span className="rounded bg-slate-100 px-2 py-1 text-xs capitalize text-slate-600">
                    {entity.risk}
                  </span>
                </div>
                <p className="mt-2 text-sm text-slate-600">{entity.normalized}</p>
                <p className="mt-1 text-xs text-slate-500">{entity.databases.join(", ")}</p>
              </div>
            ))}
          </div>
        </section>
        <section className="rounded-lg border border-slate-200 bg-white p-4">
          <h2 className="text-base font-semibold">Function Direction</h2>
          <div className="mt-4 grid gap-2">
            {result.candidate_concept.possible_function_direction.map((direction) => (
              <div key={direction} className="rounded-md bg-slate-50 px-3 py-2 text-sm text-slate-700">
                {direction}
              </div>
            ))}
          </div>
          <h3 className="mt-5 text-sm font-semibold text-slate-700">Follow-up Questions</h3>
          <div className="mt-3 flex flex-wrap gap-2">
            {result.follow_up_questions.map((question) => (
              <span key={question} className="rounded-md border border-slate-200 px-3 py-2 text-xs text-slate-600">
                {question}
              </span>
            ))}
          </div>
        </section>
      </div>
      <EvidenceDrawer evidence={result.evidence} />
    </section>
  );
}
