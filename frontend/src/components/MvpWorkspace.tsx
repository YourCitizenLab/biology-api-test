"use client";

import { useMemo, useState } from "react";
import { AgentReasoningPanel } from "@/components/AgentReasoningPanel";
import { CardLibrary } from "@/components/CardLibrary";
import { DemoCard, demoCards } from "@/components/cards";
import { DiscoveryInput } from "@/components/DiscoveryInput";
import { FollowUpChat } from "@/components/FollowUpChat";
import { ResultDashboard } from "@/components/ResultDashboard";
import { SimulationCanvas } from "@/components/SimulationCanvas";
import { simulateDiscovery, SimulationResult } from "@/lib/api";

type MvpWorkspaceProps = {
  initialView: "home" | "lab" | "result";
};

const defaultPrompt = "Making a new peptide out of bull, tiger, and blue scorpion.";
const defaultCards = ["Bull", "Tiger", "Blue Scorpion", "Peptide"];

export function MvpWorkspace({ initialView }: MvpWorkspaceProps) {
  const [prompt, setPrompt] = useState(defaultPrompt);
  const [selectedCards, setSelectedCards] = useState<string[]>(
    initialView === "home" ? defaultCards : defaultCards
  );
  const [result, setResult] = useState<SimulationResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const selectedCardObjects = useMemo(
    () => selectedCards.map((name) => demoCards.find((card) => card.name === name)).filter(Boolean),
    [selectedCards]
  );

  function addCard(card: DemoCard | string) {
    const name = typeof card === "string" ? card : card.name;
    setSelectedCards((current) => (current.includes(name) ? current : [...current, name]));
  }

  function removeCard(cardName: string) {
    setSelectedCards((current) => current.filter((name) => name !== cardName));
  }

  async function runSimulation() {
    setLoading(true);
    setError(null);
    try {
      const nextResult = await simulateDiscovery(prompt, selectedCards);
      setResult(nextResult);
    } catch (requestError) {
      setError("Backend is not reachable at the configured API URL.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="mx-auto flex max-w-7xl flex-col gap-5 px-4 py-5 sm:px-6 lg:px-8">
      <header className="flex flex-col gap-3 rounded-lg border border-slate-200 bg-white/92 p-4 shadow-surface sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h1 className="text-2xl font-semibold text-ink">Interactive AI Bio/Chem Discovery Simulator</h1>
          <p className="mt-1 text-sm text-slate-600">Concept-level demo workspace</p>
        </div>
        <nav className="flex gap-2 text-sm">
          <a className="rounded-md border border-slate-200 px-3 py-2 font-medium text-slate-700" href="/">
            Home
          </a>
          <a className="rounded-md border border-slate-200 px-3 py-2 font-medium text-slate-700" href="/lab">
            Lab
          </a>
          <a className="rounded-md border border-slate-200 px-3 py-2 font-medium text-slate-700" href="/result">
            Result
          </a>
        </nav>
      </header>

      <DiscoveryInput value={prompt} isLoading={loading} onChange={setPrompt} onSubmit={runSimulation} />
      {error && <div className="rounded-md border border-red-200 bg-red-50 p-3 text-sm text-red-900">{error}</div>}

      <div className="grid gap-5 lg:grid-cols-[320px_1fr]">
        <aside className="space-y-5">
          <CardLibrary selectedCards={selectedCards} onAddCard={addCard} />
          <AgentReasoningPanel active={loading} hasResult={Boolean(result)} />
        </aside>
        <div className="space-y-5">
          <SimulationCanvas selectedCards={selectedCards} onDropCard={addCard} onRemoveCard={removeCard} />
          <div className="flex flex-wrap items-center gap-2">
            {selectedCardObjects.map((card) => (
              <span key={card!.name} className={`rounded px-2 py-1 text-xs font-semibold ${card!.accent}`}>
                {card!.name}
              </span>
            ))}
          </div>
          <ResultDashboard result={result} />
          <FollowUpChat result={result} />
        </div>
      </div>
    </main>
  );
}
