"use client";

type DiscoveryInputProps = {
  value: string;
  isLoading: boolean;
  onChange: (value: string) => void;
  onSubmit: () => void;
};

export function DiscoveryInput({ value, isLoading, onChange, onSubmit }: DiscoveryInputProps) {
  return (
    <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-surface">
      <label className="text-sm font-semibold text-slate-700" htmlFor="discovery-input">
        Discovery prompt
      </label>
      <div className="mt-3 flex flex-col gap-3 lg:flex-row">
        <textarea
          id="discovery-input"
          className="min-h-24 flex-1 resize-none rounded-md border border-slate-300 px-3 py-3 text-sm leading-6"
          value={value}
          onChange={(event) => onChange(event.target.value)}
        />
        <button
          className="rounded-md bg-ink px-5 py-3 text-sm font-semibold text-white disabled:cursor-not-allowed disabled:opacity-60"
          onClick={onSubmit}
          disabled={isLoading || !value.trim()}
        >
          {isLoading ? "Simulating" : "Generate"}
        </button>
      </div>
    </section>
  );
}
