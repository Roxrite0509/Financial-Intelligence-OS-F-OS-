import { useEffect, useState } from "react";
import { api } from "../lib/api";

import MetricCard from "../components/MetricCard";
import PriceChart from "../components/PriceChart";
import InsightBox from "../components/InsightBox";
import NotesPanel from "../components/NotesPanel";

export default function Dashboard() {
    const [symbol, setSymbol] = useState("SBIN");
    const [metrics, setMetrics] = useState<any>(null);
    const [graph, setGraph] = useState<any>(null);
    const [insight, setInsight] = useState("");

    useEffect(() => {
        api.get(`/market/stock?symbol=${symbol}`).then((res: any) =>
            setMetrics(res.data)
        );

        api.get(`/market/graph?symbol=${symbol}`).then((res: any) =>
            setGraph(res.data)
        );

        api.get(`/market/ai?symbol=${symbol}`).then((res: any) =>
            setInsight(res.data.insight)
        );
    }, [symbol]);

    if (!metrics || !graph) {
        return <p style={{ padding: 24 }}>Loading...</p>;
    }

    return (
        <div style={{ padding: 24 }}>
            <h1>{symbol} — India Bank Intelligence</h1>

            <select
                value={symbol}
                onChange={(e) => setSymbol(e.target.value)}
                style={{ marginBottom: 16 }}
            >
                <option value="SBIN">SBI</option>
                <option value="HDFCBANK">HDFC Bank</option>
                <option value="ICICIBANK">ICICI Bank</option>
                <option value="AXISBANK">Axis Bank</option>
            </select>

            <div style={{ display: "flex", gap: 16 }}>
                <MetricCard label="Price" value={metrics.price} />
                <MetricCard label="Return %" value={metrics.return_pct} />
                <MetricCard label="Volatility" value={metrics.volatility} />
            </div>

            <PriceChart data={graph.series} />
            <InsightBox insight={insight} />
            <NotesPanel symbol={symbol} />
        </div>
    );
}
