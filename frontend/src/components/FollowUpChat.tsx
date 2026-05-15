"use client";

import { useState } from "react";
import { askFollowUp, FollowUpResponse, SimulationResult } from "@/lib/api";

type Message = {
  role: "user" | "assistant";
  text: string;
};

export function FollowUpChat({ result }: { result: SimulationResult | null }) {
  const [input, setInput] = useState("Can this concept be made safer?");
  const [messages, setMessages] = useState<Message[]>([]);
  const [actions, setActions] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  async function submit() {
    if (!input.trim()) return;
    const userMessage = input.trim();
    setInput("");
    setMessages((current) => [...current, { role: "user", text: userMessage }]);
    setLoading(true);
    try {
      const response: FollowUpResponse = await askFollowUp(userMessage, result);
      setMessages((current) => [...current, { role: "assistant", text: response.answer }]);
      setActions(response.suggested_actions);
    } catch (error) {
      setMessages((current) => [
        ...current,
        { role: "assistant", text: "The follow-up service is not reachable yet." },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-surface">
      <h2 className="text-base font-semibold">Follow-up Chat</h2>
      <div className="mt-4 min-h-28 space-y-2 rounded-md bg-slate-50 p-3">
        {messages.length === 0 ? (
          <p className="text-sm text-slate-500">Ask a safety-aware follow-up after simulation.</p>
        ) : (
          messages.map((message, index) => (
            <p
              key={`${message.role}-${index}`}
              className={`rounded-md px-3 py-2 text-sm ${
                message.role === "user" ? "bg-white text-ink" : "bg-teal-50 text-teal-950"
              }`}
            >
              {message.text}
            </p>
          ))
        )}
      </div>
      <div className="mt-3 flex flex-col gap-2 sm:flex-row">
        <input
          className="min-h-11 flex-1 rounded-md border border-slate-300 px-3 text-sm"
          value={input}
          onChange={(event) => setInput(event.target.value)}
        />
        <button
          className="rounded-md bg-signal px-4 py-2 text-sm font-semibold text-white disabled:opacity-60"
          onClick={submit}
          disabled={loading || !result}
        >
          {loading ? "Asking" : "Send"}
        </button>
      </div>
      {actions.length > 0 && (
        <div className="mt-3 flex flex-wrap gap-2">
          {actions.map((action) => (
            <span key={action} className="rounded-md bg-slate-100 px-3 py-2 text-xs text-slate-600">
              {action}
            </span>
          ))}
        </div>
      )}
    </section>
  );
}
