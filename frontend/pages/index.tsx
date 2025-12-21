import Link from "next/link";

export default function Home() {
    return (
        <div className="h-screen bg-black text-white flex items-center justify-center">
            <div className="space-y-4 text-center">
                <h1 className="text-4xl font-bold">F-OS</h1>
                <p className="text-gray-400">Bank Monitoring System</p>
                <Link
                    href="/dashboard"
                    className="inline-block px-6 py-3 bg-yellow-500 text-black rounded"
                >
                    Go to Dashboard
                </Link>
            </div>
        </div>
    );
}
