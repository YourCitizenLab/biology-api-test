import type { RiskLevel, SuggestedCard } from "@/lib/api";

export type DemoCard = {
  name: string;
  category: string;
  risk: RiskLevel;
  accent: string;
};

export const demoCards: DemoCard[] = [
  { name: "Bull", category: "Animal Source", risk: "low", accent: "bg-sky-100 text-sky-900" },
  { name: "Tiger", category: "Animal Source", risk: "low", accent: "bg-amber-100 text-amber-900" },
  { name: "Blue Scorpion", category: "Animal Source", risk: "high", accent: "bg-rose-100 text-rose-900" },
  { name: "Peptide", category: "Biomolecule", risk: "medium", accent: "bg-teal-100 text-teal-900" },
  { name: "Antimicrobial Peptide", category: "Biomolecule", risk: "medium", accent: "bg-emerald-100 text-emerald-900" },
  { name: "Plant Peptide", category: "Biomolecule", risk: "low", accent: "bg-lime-100 text-lime-900" },
  { name: "PubChem", category: "Database", risk: "low", accent: "bg-slate-100 text-slate-900" },
  { name: "UniProt", category: "Database", risk: "low", accent: "bg-indigo-100 text-indigo-900" },
  { name: "ChEMBL", category: "Database", risk: "low", accent: "bg-fuchsia-100 text-fuchsia-900" },
  { name: "RCSB PDB", category: "Database", risk: "low", accent: "bg-cyan-100 text-cyan-900" },
];

const accentByCategory: Record<string, string> = {
  "Animal Source": "bg-sky-100 text-sky-900",
  Biomolecule: "bg-emerald-100 text-emerald-900",
  Database: "bg-indigo-100 text-indigo-900",
  "Safer Alternative": "bg-lime-100 text-lime-900",
  Function: "bg-amber-100 text-amber-900",
  "Risk Context": "bg-rose-100 text-rose-900",
};

export function toDemoCard(card: SuggestedCard): DemoCard {
  const existing = demoCards.find((item) => item.name === card.name);
  if (existing) {
    return existing;
  }

  return {
    name: card.name,
    category: card.category,
    risk: card.risk,
    accent: accentByCategory[card.category] ?? "bg-slate-100 text-slate-900",
  };
}
