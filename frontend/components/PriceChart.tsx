export default function MetricCard({ label, value }: any) {
    return (
        <div style={{ padding: 16, background: "#111", color: "#fff", borderRadius: 8 }}>
            <div style={{ opacity: 0.6 }}>{label}</div>
            <div style={{ fontSize: 20 }}>{value}</div>
        </div>
    );
}
