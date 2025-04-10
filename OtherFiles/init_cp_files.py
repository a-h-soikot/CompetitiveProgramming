# This script initializes or updates C++ files in a specified directory with a template for competitive programming.
# It also empties any .txt files in the same directory.

import os

# Target directory
folder_path = '/home/soikot/Documents/Contest'

# Template for .cpp files
cpp_template = r"""#include <bits/stdc++.h>
using namespace std;

template<typename T3> void write(T3 zZ) { cout << zZ << endl; }
template<typename T, typename... T2> void write(T zZ, T2... more) { cout << zZ << ' '; write(more...); }

const int64_t mod = 1e9 + 7;
#define int long long
#define pb push_back
#define pii pair<int, int>
#define ff first
#define ss second
#define vi vector<int>
#define sz(a) ((int)(a.size()))
#define mp(a, b) make_pair(a, b)
#define all(a) a.begin(), a.end()
#define read(a) for(auto &i : a) cin >> i
#define rep(i, a, n) for(int i = a; i < n; i++)
#define print(a) for(auto x : a) cout << x << " "

void solve (void) {
    
}

signed main()
{
    ios_base::sync_with_stdio(false); cin.tie(nullptr);

    int tests = 1; cin >> tests;

    while(tests--) { solve(); if(tests) cout << '\n'; }

    return 0;
}
"""

# Loop through all files in the folder
files = [filename for filename in os.listdir(folder_path)]
files.sort()

for filename in files:
    full_path = os.path.join(folder_path, filename)

    if filename.endswith(".cpp"):
        with open(full_path, 'w') as f:
            f.write(cpp_template)
        print(f"Updated: {filename} with CP template")

    elif filename.endswith(".txt"):
        with open(full_path, 'w') as f:
            f.truncate(0)  # Empty the file
        print(f"Emptied: {filename}")


print("Operation complete.")