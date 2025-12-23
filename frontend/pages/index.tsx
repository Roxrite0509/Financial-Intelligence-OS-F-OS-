import Link from "next/link";

export default function Home() {
    return (
        <div style={{ padding: 32 }}>
            <h1>F-OS India Bank Intelligence</h1>

            <p>
                India-first banking & market intelligence platform.
            </p>

            <ul>
                <li>
                    <Link href="/dashboard">📊 Dashboard</Link>
                </li>
                <li>
                    <Link href="/markets">🏦 Bank Markets</Link>
                </li>
                <li>
                    <Link href="/ai">🤖 AI Insights</Link>
                </li>
            </ul>
        </div>
    );
}
