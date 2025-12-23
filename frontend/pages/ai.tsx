import { useState } from "react";
import axios from "axios";

export default function AI() {
    const [text, setText] = useState("");

    const run = async () => {
        const res = await axios.get(
            "http://127.0.0.1:8000/market/ai?symbol=SBIN.NS"
        );
        setText(res.data.insight);
    };

    return (
        <div>
            <h2>AI Insight</h2>
            <button onClick={run}>Explain SBIN</button>
            <pre>{text}</pre>
        </div>
    );
}
