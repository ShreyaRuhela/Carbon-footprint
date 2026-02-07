#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

/**
 * SUSTAINABILITY SCORECARD GENERATOR
 * This utility creates a final summary report for the user's current session.
 * It follows standard C++ best practices.
 */

struct EmissionEntry {
    string category;
    double kg;
};

class ScorecardGenerator {
public:
    void printHeader() {
        cout << "\n" << string(50, '=') << endl;
        cout << "        CARBON PULSE ELITE SCORECARD          " << endl;
        cout << string(50, '=') << endl;
    }

    void processData(const vector<EmissionEntry>& data) {
        double total = 0;
        cout << left << setw(20) << "CATEGORY" << setw(15) << "EMISSION (KG)" << endl;
        cout << string(50, '-') << endl;

        for (const auto& entry : data) {
            cout << left << setw(20) << entry.category << setw(15) << fixed << setprecision(2) << entry.kg << endl;
            total += entry.kg;
        }

        cout << string(50, '-') << endl;
        cout << "SESSION TOTAL: " << total << " KG CO2e" << endl;
        
        // Net Zero Calculation
        int treesNeeded = (total > 0) ? (int)(total / 21.0) + 1 : 0;
        cout << "NET ZERO REQUIREMENT: Plant " << treesNeeded << " trees this year." << endl;
        
        printVerdict(total);
    }

private:
    void printVerdict(double total) {
        cout << "\nENVIRONMENTAL VERDICT: ";
        if (total < 10.0) cout << "ECO-CONSCIOUS" << endl;
        else if (total < 50.0) cout << "AVERAGE IMPACT" << endl;
        else cout << "CRITICAL ALERT: HIGH IMPACT" << endl;
        cout << string(50, '=') << "\n" << endl;
    }
};

int main() {
    ScorecardGenerator generator;
    
    // Sample session data matching our React logs
    vector<EmissionEntry> sessionData = {
        {"Transport", 12.80},
        {"Food", 4.50},
        {"Digital", 0.60},
        {"Home Energy", 18.20},
        {"Shopping", 3.40}
    };

    generator.printHeader();
    generator.processData(sessionData);

    return 0;
}