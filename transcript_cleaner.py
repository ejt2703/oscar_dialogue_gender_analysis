import re
import csv
import os

class TranscriptCleaner:
    def __init__(self, transcript_file):
        self.transcript_file = transcript_file
        self.dialogue_entries = []
    
    def extract_dialogue_lines(self):
        """Extract dialogue from transcript, removing stage directions"""
        print("\n📖 Extracting dialogue from transcript...")
        
        with open(self.transcript_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        dialogue_lines = []
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Skip obvious non-dialogue
            if line.startswith('*') or line.startswith('#') or line.startswith('[Skip to'):
                continue
            
            # Remove all stage directions/actions in brackets
            cleaned = re.sub(r'\[.*?\]', '', line)
            
            # Remove music notes
            cleaned = re.sub(r'[♪♫]', '', cleaned)
            
            # Remove parenthetical stage directions
            cleaned = re.sub(r'\(.*?\)', '', cleaned)
            
            # Clean up extra whitespace
            cleaned = ' '.join(cleaned.split())
            
            # Only keep lines with actual dialogue
            if cleaned and len(cleaned) > 0:
                dialogue_lines.append(cleaned)
        
        print(f"✓ Extracted {len(dialogue_lines)} dialogue lines")
        return dialogue_lines
    
    def count_words(self, text):
        """Count words in dialogue"""
        words = text.split()
        return len(words)
    
    def process_dialogue(self, dialogue_lines):
        """Process all dialogue lines"""
        print("\n📊 Processing dialogue...")
        
        for line in dialogue_lines:
            # Convert to uppercase
            dialogue_clean = line.upper()
            
            # Count words
            word_count = self.count_words(line)
            
            # Create entry with UNKNOWN for speaker/gender
            entry = {
                'speaker': 'UNKNOWN',
                'speaker_gender': 'UNKNOWN',
                'dialogue': dialogue_clean,
                'word_count': word_count
            }
            
            self.dialogue_entries.append(entry)
        
        print(f"✓ Processed {len(self.dialogue_entries)} dialogue entries")
    
    def export_to_csv(self, output_file):
        """Export dialogue to CSV"""
        print(f"\n💾 Exporting to {output_file}...")
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'speaker', 'speaker_gender', 'dialogue', 'word_count'
            ])
            
            writer.writeheader()
            writer.writerows(self.dialogue_entries)
        
        print(f"✓ Exported {len(self.dialogue_entries)} entries to {output_file}")
    
    def run(self, output_file):
        """Run the complete analysis"""
        print("\n" + "="*60)
        print("🎬 MOVIE DIALOGUE ANALYZER")
        print("="*60)
        
        dialogue_lines = self.extract_dialogue_lines()
        self.process_dialogue(dialogue_lines)
        self.export_to_csv(output_file)
        
        print("\n" + "="*60)
        print("✅ ANALYSIS COMPLETE!")
        print("✏️  Open the CSV to add speaker names and genders")
        print("="*60)


# Main execution
if __name__ == "__main__":
    print("\n🎬 TRANSCRIPT CLEANER")
    print("="*60)
    
    # Get file paths from user
    transcript_file = input("\nEnter transcript file path (e.g., anora_transcript.txt): ").strip()
    output_file = input("Enter output CSV file path (e.g., anora_output.csv): ").strip()
    
    # Check if file exists
    if not os.path.exists(transcript_file):
        print(f"❌ Error: {transcript_file} not found!")
        exit(1)
    
    # Run analyzer
    analyzer = TranscriptCleaner(transcript_file)
    analyzer.run(output_file)