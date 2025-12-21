import Link from "next/link";

export default function Sidebar() {
    return (
        <div className="sidebar">
            <h2 style={{ color: "#facc15", marginBottom: 20 }}>F-OS</h2>

            <Link href="/dashboard">Dashboard</Link>
            <Link href="/markets">Markets</Link>
            <Link href="/macro">Macro</Link>
            <Link href="/ai">AI Insights</Link>
            <Link href="/about">About</Link>
        </div>
    );
}
