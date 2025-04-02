import os
import asyncio
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
from pydub import AudioSegment  # pip install pydub

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("CAIS_TTS_OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("Please set your CAIS_TTS_OPENAI_API_KEY in the .env file.")

# Initialize the OpenAI client
client = OpenAI(api_key=API_KEY)

# Define your text chunks (feel free to adjust these as needed)

text_0 = (
    "Rapid advances in AI are beginning to reshape national security. Destabilizing AI developments could rupture the balance of power and raise the odds of great-power conflict, while widespread proliferation of capable AI hackers and virologists would lower barriers for rogue actors to cause catastrophe. Superintelligence—AI vastly better than humans at nearly all cognitive tasks—is now anticipated by AI researchers. Just as nations once developed nuclear strategies to secure their survival, we now need a coherent superintelligence strategy to navigate a new period of transformative change. We introduce the concept of Mutual Assured AI Malfunction or MAIM: a deterrence regime resembling nuclear mutual assured destruction or MAD where any state’s aggressive bid for unilateral AI dominance is met with preventive sabotage by rivals. Given the relative ease of sabotaging a destabilizing AI project—through interventions ranging from covert cyberattacks to potential kinetic strikes on datacenters—MAIM already describes the strategic picture AI superpowers find themselves in. Alongside this, states can increase their competitiveness by bolstering their economies and militaries through AI, and they can engage in nonproliferation to rogue actors to keep weaponizable AI capabilities out of their hands. Taken together, the three-part framework of deterrence, nonproliferation, and competitiveness outlines a robust strategy to superintelligence in the years ahead.\n"
    "\n"
)

text_1 = (
    "Introduction.\n"
    "\n"
    "From geopolitical conflict to catastrophic misuse, the challenges AI poses are far too broad, and far too serious, for piecemeal measures. What is needed is a comprehensive approach, one that does not shy from the unsettling implications of advanced AI. As with Herman Kahn’s famous analysis of nuclear strategy , superintelligence strategy requires “thinking about the unthinkable.” An effective strategy should draw from a long history of national security policy because superintelligence is inescapably a matter of national security.\n"
    "\n"
    "AI lowers barriers for acts of mass destruction once the exclusive domain of major powers. Individuals armed with an expert-level AI virologist could create novel pathogens, while advanced hacking AIs might target energy grids at a national scale. Defense often lags behind offense in both biology and critical infrastructure, leaving large swaths of civilization vulnerable. The relative security we enjoyed when only nation-states were capable of sophisticated attacks will no longer hold if highly capable AIs can guide extremist cells from plan to execution.\n"
    "\n"
    "Militaries see in AI the key to a decisive edge, igniting a race to develop capabilities that could overturn existing balances of power. Beyond powering next-generation drones, AI raises the specter of strategic breakthroughs that might upend nuclear deterrence. A superintelligence—if its creators can control it—could conceivably deliver a “superweapon” and hand its wielders a strategic monopoly on power . Superintelligence is not merely a new weapon, but a way to fast-track all future military innovation. A nation with sole possession of superintelligence might be as overwhelming as the Conquistadors were to the Aztecs. In a winner-take-all race, any hint of a looming superweapon fuels tensions, pushing rivals toward actions that could quickly escalate into open conflict. AI development is fast becoming a matter of survival rather than merely technological ambition.\n"
    "\n"
    "Another hazard emerges when AI systems can autonomously develop the next generation of AIs. Systems that can fully automate the AI research process could telescope a decade of progress into a year. A fast feedback loop could create an “intelligence explosion,” resulting in AIs as uncontainable to us as an adult would be to a group of three-year-olds. Racing countries might forgo human oversight of automated research, since it would slow research from machine speed to human speed. If AI systems outpace the safeguards designed for them, we may accidentally unleash an AI which does not follow a commander’s intent.\n"
    "\n"
    "In this paper, we propose a superintelligence strategy emphasizing three key pillars of deterrence, competitiveness, and nonproliferation. We introduce Mutual Assured AI Malfunction or MAIM, arguing that when states possess common knowledge of the national security implications of AI, they will each act to sabotage rival AI projects that threaten their security. MAIM might be used to create a stable deterrence regime, preventing mutual assured AI destruction from escalating into mutual assured human destruction. Meanwhile, governments which rely exclusively on Taiwan for crucial chips leave themselves vulnerable to crippling disruption if tensions escalate. In order to retain economic and military competitiveness in a shifting landscape, nations must secure domestic supply chains for AI chips and drones. Finally, all nations have a shared interest in nonproliferation efforts to limit the AI capabilities accessible to rogue actors. Through these pillars, states can safeguard their security while opening the door to unprecedented prosperity.\n"
    "\n"
    "Though this abridged paper describes the core of our strategy, we recommend the comprehensive version of this paper—“Superintelligence Strategy: Expert Version”—for those interested in a more detailed strategic analysis covering a broader range of challenges.\n"
    "\n"
    "Existing Strategies.\n"
)

text_2 = (
    "States grappling with terrorist threats, destabilizing weaponization capabilities, and the specter of losing control to AI face difficult choices on how to preserve themselves in a shifting landscape. Against this backdrop, three proposals have gained prominence: the first lifts all restraints on development and dissemination, treating AI like just another computer application; the second envisions a voluntary halt when programs cross a danger threshold, hoping that every great power will collectively stand down; and the third advocates concentrating development in a single, government-led project that seeks a strategic monopoly over the globe. Each path carries its own perils, inviting either malicious use risks, toothless treaties, or a destabilizing bid for dominance. Here we briefly examine these three strategies and highlight their flaws.\n"
    "\n"
    "1.  Hands-off (“Move Fast and Break Things”, or “YOLO”) Strategy. This strategy advocates for no restrictions on AI developers, AI chips, and AI models. Proponents of this strategy insist that the US government impose no requirements—including testing for weaponization capabilities—on AI companies, lest it curtail innovation and allow China to win. They likewise oppose export controls on AI chips, claiming such measures would concentrate power and enable a one-world government; in their view, these chips should be sold to whoever can pay, including adversaries. Finally, they encourage that advanced US model weights continue to be released openly, arguing that even if China or rogue actors use these AIs, no real security threat arises because, they maintain, AI’s capabilities are defense-dominant. From a national security perspective, this is neither a credible nor a coherent strategy.\n"
    "\n"
    "2.  Moratorium Strategy. The voluntary moratorium strategy proposes halting AI development—either immediately or once certain hazardous capabilities, such as hacking or autonomous operation, are detected. Proponents assume that if an AI model test crosses a hazard threshold, major powers will pause their programs. Yet militaries desire precisely these hazardous capabilities, making reciprocal restraint implausible. Even with a treaty, the absence of verification mechanisms means the treaty would be toothless; each side, fearing the other’s secret work, would simply continue. Without the threat of force, treaties will be reneged, and some states will pursue an intelligence recursion. This dynamic, reminiscent of prior arms-control dilemmas, renders the voluntary moratorium more an aspiration than a viable plan.\n"
    "\n"
    "3.  Monopoly Strategy. The Monopoly strategy envisions one project securing a monopoly over advanced AI. A less-cited variant—a CERN for AI reminiscent of the Baruch Plan from the atomic era—suggests an international consortium to lead AI development, but this has gained less policymaker interest. By contrast, the US-China Economic and Security Review Commission has suggested a more offensive path: a Manhattan Project to build superintelligence. Such a project would invoke the Defense Production Act to channel AI chips into a US desert compound staffed by top researchers, a large fraction of whom are necessarily Chinese nationals, with the stated goal of developing superintelligence to gain a strategic monopoly. Yet this facility, easily observed by satellite and vulnerable to preemptive attack, would inevitably raise alarm. China would not sit idle waiting to accept the US’s dictates once they achieve superintelligence or wait as they risk a loss of control. The Manhattan Project assumes that rivals will acquiesce to an enduring imbalance or omnicide rather than move to prevent it. What begins as a push for a superweapon and global control risks prompting hostile countermeasures and escalating tensions, thereby undermining the very stability the strategy purports to secure.\n"
)

# List of text chunks and corresponding temporary WAV filenames
texts = [text_0, text_1, text_2]
temp_files = [Path(f"speech_hd_{i}.wav") for i in range(len(texts))]

async def generate_audio(chunk: str, outfile: Path):
    """
    Generate speech audio for a given text chunk and save it to outfile.
    Since the OpenAI client call is synchronous, we offload it using a thread pool.
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None,
        lambda: client.audio.speech.create(
            model="tts-1-hd",
            voice="onyx",
            input=chunk,
            response_format="wav"
        )
    )
    await loop.run_in_executor(None, lambda: response.stream_to_file(outfile))
    print(f"Audio for chunk saved to: {outfile.resolve()}")

def stitch_wav_files_pydub(input_files, output_file):
    """
    Concatenate multiple WAV files using pydub.
    This method loads each file as an AudioSegment, concatenates them in order,
    and then exports the combined audio as a single WAV file.
    """
    combined = AudioSegment.empty()
    for file in input_files:
        segment = AudioSegment.from_wav(str(file))
        combined += segment
    combined.export(str(output_file), format="wav")
    print(f"Stitched audio saved to: {output_file.resolve()}")

async def main():
    # Dispatch all TTS requests concurrently
    tasks = [asyncio.create_task(generate_audio(chunk, outfile))
             for chunk, outfile in zip(texts, temp_files)]
    await asyncio.gather(*tasks)
    
    # Once all audio files are generated, concatenate them using pydub
    final_output = Path("final_output.wav")
    stitch_wav_files_pydub(temp_files, final_output)

if __name__ == '__main__':
    asyncio.run(main())



