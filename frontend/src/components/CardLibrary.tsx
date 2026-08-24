"use client";

import { DemoCard } from "@/components/cards";

type CardLibraryProps = {
  generatedCards: DemoCard[];
  canvasCards: string[];
};

export function CardLibrary({ generatedCards, canvasCards }: CardLibraryProps) {
  return (
    <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-surface">
      <div className="flex items-center justify-between gap-3">
        <h2 className="text-base font-semibold">Card Library</h2>
        <span className="text-xs font-medium text-slate-500">{generatedCards.length} generated</span>
      </div>
      <p className="mt-2 text-sm text-slate-500">Generate cards from the prompt, then drag the ones you want into the simulation canvas.</p>
      <div className="mt-4 grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-2">
        {generatedCards.length === 0 ? (
          <div className="col-span-full rounded-md border border-slate-200 bg-slate-50 p-4 text-sm text-slate-500">
            No prompt-derived cards yet.
          </div>
        ) : (
          generatedCards.map((card) => {
          const active = canvasCards.includes(card.name);
          return (
            <div
              draggable
              key={card.name}
              className={`rounded-md border px-3 py-3 text-left transition hover:border-slate-500 ${
                active ? "border-ink bg-slate-50" : "border-slate-200 bg-white"
              }`}
              onDragStart={(event) => event.dataTransfer.setData("text/plain", card.name)}
            >
              <span className={`inline-flex rounded px-2 py-1 text-xs font-semibold ${card.accent}`}>
                {card.category}
              </span>
              <span className="mt-2 block text-sm font-semibold text-ink">{card.name}</span>
              <span className="mt-1 block text-xs capitalize text-slate-500">Risk: {card.risk}</span>
              <span className="mt-3 block text-xs text-slate-400">{active ? "Already on canvas" : "Drag to canvas"}</span>
            </div>
          );
        }))}
      </div>
    </section>
  );
}
