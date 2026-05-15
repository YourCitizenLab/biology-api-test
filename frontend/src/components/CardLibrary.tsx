"use client";

import { DemoCard, demoCards } from "@/components/cards";

type CardLibraryProps = {
  selectedCards: string[];
  onAddCard: (card: DemoCard) => void;
};

export function CardLibrary({ selectedCards, onAddCard }: CardLibraryProps) {
  return (
    <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-surface">
      <div className="flex items-center justify-between gap-3">
        <h2 className="text-base font-semibold">Card Library</h2>
        <span className="text-xs font-medium text-slate-500">{selectedCards.length} selected</span>
      </div>
      <div className="mt-4 grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-2">
        {demoCards.map((card) => {
          const active = selectedCards.includes(card.name);
          return (
            <button
              draggable
              key={card.name}
              className={`rounded-md border px-3 py-3 text-left transition hover:border-slate-500 ${
                active ? "border-ink bg-slate-50" : "border-slate-200 bg-white"
              }`}
              onClick={() => onAddCard(card)}
              onDragStart={(event) => event.dataTransfer.setData("text/plain", card.name)}
            >
              <span className={`inline-flex rounded px-2 py-1 text-xs font-semibold ${card.accent}`}>
                {card.category}
              </span>
              <span className="mt-2 block text-sm font-semibold text-ink">{card.name}</span>
              <span className="mt-1 block text-xs capitalize text-slate-500">Risk: {card.risk}</span>
            </button>
          );
        })}
      </div>
    </section>
  );
}
