"use client";

type SimulationCanvasProps = {
  selectedCards: string[];
  onDropCard: (cardName: string) => void;
  onRemoveCard: (cardName: string) => void;
};

export function SimulationCanvas({ selectedCards, onDropCard, onRemoveCard }: SimulationCanvasProps) {
  return (
    <section
      className="min-h-52 rounded-lg border border-dashed border-slate-300 bg-slate-50 p-4"
      onDragOver={(event) => event.preventDefault()}
      onDrop={(event) => {
        event.preventDefault();
        const cardName = event.dataTransfer.getData("text/plain");
        if (cardName) onDropCard(cardName);
      }}
    >
      <div className="flex items-center justify-between gap-3">
        <h2 className="text-base font-semibold">Simulation Canvas</h2>
        <span className="text-xs font-medium text-slate-500">Drag cards here, then run the simulation</span>
      </div>
      <div className="mt-4 flex min-h-32 flex-wrap gap-2">
        {selectedCards.length === 0 ? (
          <div className="flex w-full items-center justify-center rounded-md border border-slate-200 bg-white p-6 text-sm text-slate-500">
            Drop prompt-generated cards here
          </div>
        ) : (
          selectedCards.map((card) => (
            <button
              key={card}
              className="h-16 rounded-md border border-slate-300 bg-white px-4 text-sm font-semibold text-ink shadow-sm"
              onClick={() => onRemoveCard(card)}
              title={`Remove ${card}`}
            >
              {card}
            </button>
          ))
        )}
      </div>
    </section>
  );
}
