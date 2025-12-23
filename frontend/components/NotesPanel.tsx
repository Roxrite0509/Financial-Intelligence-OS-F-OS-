import { useState } from "react";

export default function NotesPanel({ symbol }: any) {
    const [note, setNote] = useState("");

    return (
        <div style={{ marginTop: 20 }}>
            <h3>Notes</h3>
            <textarea
                value={note}
                onChange={(e) => setNote(e.target.value)}
                style={{ width: "100%", height: 100 }}
            />
        </div>
    );
}
