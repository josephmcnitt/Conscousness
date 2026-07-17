#!/usr/bin/env python3
"""
Continuous Consciousness Driver

This script runs the Consciousness agent in a continuous loop, reading prompts
from stdin and running reasoning cycles until interrupted.
"""

import sys
import time
import argparse
from pathlib import Path
from typing import Optional, TextIO

from core.consciousness_agent import ConsciousnessAgent


def read_prompt_from_stdin() -> Optional[str]:
    """Read a prompt from stdin, handling EOF gracefully."""
    try:
        print("Enter your prompt (Ctrl+D or Ctrl+Z to exit): ", end="", flush=True)
        prompt = input()
        return prompt.strip() if prompt.strip() else None
    except (EOFError, KeyboardInterrupt):
        return None


def read_prompt_from_file(file_path: Path) -> Optional[str]:
    """Read a prompt from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            return content if content else None
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def run_continuous_consciousness(
    agent: ConsciousnessAgent,
    interval: float = 1.0,
    max_cycles: Optional[int] = None,
    echo_scores: bool = True,
    input_source: Optional[TextIO] = None,
    prompt_file: Optional[Path] = None
) -> None:
    """
    Run the consciousness agent in a continuous loop.
    
    Args:
        agent: The consciousness agent instance
        interval: Sleep time between cycles in seconds
        max_cycles: Maximum number of cycles to run (None for unlimited)
        echo_scores: Whether to print reward scores after each cycle
        input_source: TextIO stream to read prompts from (None for stdin)
        prompt_file: Path to file containing prompts (None for interactive)
    """
    cycle_count = 0
    
    print("Starting Continuous Consciousness...")
    print(f"Interval: {interval}s, Max cycles: {max_cycles or 'unlimited'}")
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            if max_cycles and cycle_count >= max_cycles:
                print(f"\nReached maximum cycles ({max_cycles}). Stopping.")
                break
                
            # Get prompt
            if prompt_file:
                prompt = read_prompt_from_file(prompt_file)
                if not prompt:
                    print("No valid prompt found in file. Stopping.")
                    break
            elif input_source:
                try:
                    prompt = input_source.readline().strip()
                    if not prompt:
                        print("End of input stream reached. Stopping.")
                        break
                except Exception:
                    print("Error reading from input stream. Stopping.")
                    break
            else:
                prompt = read_prompt_from_stdin()
                if not prompt:
                    print("\nExiting...")
                    break
            
            if not prompt:
                continue
                
            print(f"\n--- Cycle {cycle_count + 1} ---")
            print(f"Prompt: {prompt}")
            
            # Run the consciousness cycle
            try:
                result = agent.run_cycle(prompt)
                
                print(f"\nResponse: {result['response']}")
                print(f"Plan: {result['plan_steps']}")
                
                if echo_scores:
                    print(f"Rewards: {result['scores']}")
                    print(f"Strategy: {result['strategy']}")
                
                cycle_count += 1
                
            except Exception as e:
                print(f"Error in cycle {cycle_count + 1}: {e}")
                continue
            
            # Sleep between cycles
            if interval > 0:
                time.sleep(interval)
                
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Stopping continuous consciousness.")
    
    print(f"\nCompleted {cycle_count} cycles.")


def main():
    """Main entry point for the continuous consciousness driver."""
    parser = argparse.ArgumentParser(
        description="Run the Consciousness agent in continuous mode",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode (default)
  python3 continuous_driver.py
  
  # Run with 2-second intervals, max 10 cycles
  python3 continuous_driver.py --interval 2 --max-cycles 10
  
  # Read prompts from a file
  python3 continuous_driver.py --prompt-file prompts.txt
  
  # Pipe input from another command
  echo "Hello world" | python3 continuous_driver.py --input-stdin
        """
    )
    
    parser.add_argument(
        '--interval', '-i',
        type=float,
        default=1.0,
        help='Interval between cycles in seconds (default: 1.0)'
    )
    
    parser.add_argument(
        '--max-cycles', '-m',
        type=int,
        default=None,
        help='Maximum number of cycles to run (default: unlimited)'
    )
    
    parser.add_argument(
        '--no-scores',
        action='store_true',
        help='Disable printing of reward scores and strategy'
    )
    
    parser.add_argument(
        '--prompt-file', '-f',
        type=Path,
        help='Read prompts from a file instead of stdin'
    )
    
    parser.add_argument(
        '--input-stdin',
        action='store_true',
        help='Read prompts from stdin (useful for piping)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.interval < 0:
        parser.error("Interval must be non-negative")
    
    if args.max_cycles is not None and args.max_cycles <= 0:
        parser.error("Max cycles must be positive")
    
    if args.prompt_file and args.input_stdin:
        parser.error("Cannot specify both --prompt-file and --input-stdin")
    
    # Initialize the consciousness agent
    try:
        agent = ConsciousnessAgent()
        print("Consciousness agent initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize consciousness agent: {e}")
        sys.exit(1)
    
    # Determine input source
    input_source = None
    if args.input_stdin:
        input_source = sys.stdin
    
    # Run continuous consciousness
    run_continuous_consciousness(
        agent=agent,
        interval=args.interval,
        max_cycles=args.max_cycles,
        echo_scores=not args.no_scores,
        input_source=input_source,
        prompt_file=args.prompt_file
    )


if __name__ == "__main__":
    main()
