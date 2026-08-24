"use client";

import type { EvidenceItem } from "@/lib/api";

export function EvidenceDrawer({ evidence }: { evidence: EvidenceItem[] }) {
  return (
    <section className="rounded-lg border border-slate-200 bg-white p-4">
      <h2 className="text-base font-semibold">Evidence Cards</h2>
      <div className="mt-4 grid gap-3 md:grid-cols-2">
        {evidence.map((item) => (
          <article key={item.source} className="rounded-md border border-slate-200 p-3">
            <div className="flex items-start justify-between gap-3">
              <h3 className="text-sm font-semibold text-ink">{item.source}</h3>
              <span className="rounded bg-slate-100 px-2 py-1 text-xs font-medium text-slate-600">
                {item.confidence}
              </span>
            </div>
            <p className="mt-2 text-sm leading-6 text-slate-600">{item.summary}</p>
            <p className="mt-2 text-xs text-slate-500">Records: {item.records_found}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
