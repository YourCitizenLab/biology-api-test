"use client";

type AgentReasoningPanelProps = {
  active: boolean;
  hasResult: boolean;
};

const steps = [
  "Understanding input",
  "Mapping entities",
  "Checking public evidence",
  "Applying safety filter",
  "Formatting concept result",
];

export function AgentReasoningPanel({ active, hasResult }: AgentReasoningPanelProps) {
  return (
    <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-surface">
      <h2 className="text-base font-semibold">Agent Trace</h2>
      <div className="mt-4 space-y-2">
        {steps.map((step, index) => (
          <div key={step} className="flex items-center gap-3 text-sm">
            <span
              className={`flex h-7 w-7 items-center justify-center rounded-full text-xs font-semibold ${
                hasResult || (active && index < 3)
                  ? "bg-teal-100 text-teal-900"
                  : "bg-slate-100 text-slate-500"
              }`}
            >
              {index + 1}
            </span>
            <span className="text-slate-700">{step}</span>
          </div>
        ))}
      </div>
    </section>
  );
}
