export default function InsightBox({ insight }: any) {
    return (
        <div style={{ marginTop: 20, padding: 16, background: "#1a1a1a", color: "#fff" }}>
            <h3>AI Insight</h3>
            <p>{insight}</p>
        </div>
    );
}
