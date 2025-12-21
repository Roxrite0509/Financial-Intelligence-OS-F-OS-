import Sidebar from "../components/Sidebar";

export default function Dashboard() {
    return (
        <div className="layout">
            <Sidebar />

            <div className="main">
                <div className="navbar">OCDream Banking Terminal</div>

                <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr", gap: 16, marginTop: 24 }}>
                    <div className="card">
                        <h2>Market Overview</h2>
                        <p>Live prices & macro trends</p>
                    </div>

                    <div className="card">
                        <h2>Bank Snapshot</h2>
                        <p>Loans • Deposits • Risk</p>
                    </div>

                    <div className="card" style={{ gridColumn: "1 / -1" }}>
                        <h2>AI Insights</h2>
                        <p>LLM-driven analysis</p>
                    </div>
                </div>
            </div>
        </div>
    );
}
